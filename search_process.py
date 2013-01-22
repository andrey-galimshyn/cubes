import copy
from datetime import datetime
import os
import multiprocessing
import Queue


class job_message(object):
    def __init__(self, status, max, combinations, current_combination = None, searcher_ind = None):
        self.status = status
        self.max = max
        self.combinations = combinations
        self.current_combination = current_combination
        self.searcher_ind = searcher_ind


class Cube(object):
    def __init__(self, id, letters = {}):
        if len(letters) > 6:
            raise Exception('Too long list!')
        self.id = id
        self.letters = letters
        self.selected_letter = None

    def has(self,letter):
        if letter in self.letters:
            return True

    def replace_not_base(self, letter):
        for let in self.letters:
            if not self.letters[let] :
                del self.letters[let]
                self.letters[letter] = False  # False because added letter is never base
                return True

    def get_not_base(self):
        for let in self.letters:
            if not self.letters[let] :
                return let

    def letters_healthe(self) :
        if len(letters) != 6:
            raise Exception('CUBE has wrong number of LETTERS')

class Free_Cubes(object):
    def __init__(self, cubes = []):
        self.cubes = cubes

    def get_by_letter(self, letter):
       for cube in self.cubes:
            if cube.has(letter):
                self.cubes[:] = [x for x in self.cubes if x.id != cube.id]
                cube.selected_letter = letter
                return cube

    def get_back(self, rcubes):
        self.cubes.extend(rcubes)
        self.cubes = sorted(self.cubes, cmp=numeric_cubes_compare)

    def replace_not_base(self, letter_missing) :
        for cube in self.cubes:
            if cube.replace_not_base(letter_missing) :
                self.cubes[:] = [x for x in self.cubes if x != cube]
                cube.selected_letter = letter_missing
                return cube

    def self_string_presentation(self, word = 'jazz') :
        cubes_ordered = sorted(self.cubes, cmp=numeric_cubes_compare)
        rs = ''
        ordered_letters = ''
        for ordered_cube in cubes_ordered :
            try:
                ordered_letters = str(ordered_cube.id) + '. '
                for key, val in ordered_cube.letters.iteritems() :
                    ordered_letters += key + ' : ' + str(val) + ', '
            except KeyError:
                f = open('suspense.txt', 'w')
                f.write('------------------------ BEGGGGIN---------------\n')
                f.write(word.encode('utf8'))
                f.close()
                raise
            rs += ' ' + ordered_letters
        return rs

    def self_simple_string_presentation(self, word = 'jazz') :
        cubes_ordered = sorted(self.cubes, cmp=numeric_cubes_compare)
        rs = ''
        ordered_letters = ''
        for ordered_cube in cubes_ordered :
            try:
                ordered_letters = sorted(ordered_cube.letters)
            except :
                f = open('suspense.txt', 'w')
                f.write('------------------------ BEGGGGIN---------------\n')
                f.write(word.encode('utf8'))
                f.close()
                raise
            rs += ''.join(ordered_letters)

        if len(rs) != 96 :
            print 'wrong number of letters: ', len(rs)
            f = open('suspense.txt', 'w')
            f.write('------------------------ BEGGGGIN---------------\n')
            f.write(word + '\n')
            f.write(rs + '\n')
            f.close()
            raise Exception("wrong number of letters!")

        return rs

    def self_letters_healthe(self) :
        for cube in self.cubes:
            if len(cube.letters) != 6 :
                raise Exception(">>>FREE CUBES HAS WRONG NUMBER OF LETTERS!")

# If there are no cubes with desired letter, but there is a cube
# with this letter into used cubes but this letter is not used on it
# and in free cubes is a letter used on used cube with desired letter
def painless_replacement(letter, collection, free_cubes) :
    for cube in collection :
        if letter != cube.selected_letter and cube.has(letter) :
            popular_cube = free_cubes.get_by_letter(cube.selected_letter)
            if popular_cube :
                popular_cube.selected_letter = cube.selected_letter
                cube.selected_letter = letter
                return popular_cube

# If there are no cubes with desired letter
# we are searching for letter in selected cubes and 
# if this letter is not selected we may exchange letters
def exchange_letters(letter, collection, free_cubes) :
    for cube in collection :
        if letter != cube.selected_letter and cube.has(letter) :
            for cube_t in free_cubes.cubes :
                for key, val in cube_t.letters.iteritems() :
                    if key not in cube.letters :
                        cube.letters.update({key : val})
                        del cube_t.letters[key]
                        cube_t.letters[letter] = cube.letters[letter]
                        del cube.letters[letter]
                        cube_t.selected_letter = letter
                        free_cubes.cubes.remove(cube_t)
                        return cube_t

def replace_not_base_and_exchange(letter, collection, free_cubes) :
    for cube in collection :
        if letter != cube.selected_letter :
            let_buy = cube.get_not_base() 
            if let_buy :
                for cube_t in free_cubes.cubes :
                    for key, val in cube_t.letters.iteritems() :
                        if key not in cube.letters :
                            del cube.letters[let_buy]
                            cube.letters.update({key : val})
                            del cube_t.letters[key]
                            cube_t.letters[letter] = False
                            cube_t.selected_letter = letter
                            free_cubes.cubes.remove(cube_t)
                            return cube_t

def combinazione_healthe(comb, place_descr) :
    for cc in comb :
        if len(cc.letters) != 6 :
            raise Exception("wrong number of letters! after : ", place_descr)

def collect_word2(word, free_cubes, check_file) :
    if len(word) == 0:
        return None
    combinazione = []
    combinazione_candidate = None
    word=word.decode('utf-8')
    word_index = 0

    for l in word:
        lc = free_cubes.get_by_letter(l.encode('utf-8'))
        if lc :
            combinazione.append(lc)
        else :
            pr = painless_replacement(l.encode('utf-8'), combinazione, free_cubes)
            if pr and len(pr.letters) != 6 :
                raise Exception("wrong number of letters! after painless_replacement")
            if pr :
                combinazione.append(pr)
            else:
                combinazione_candidate = copy.deepcopy(combinazione)
                free_cubes_candidate = copy.deepcopy(free_cubes)
                wi = 0
                for l_candidate in word[word_index:] :
                    wi += 1
                    extra_cube = free_cubes_candidate.get_by_letter(l_candidate.encode('utf-8'))
                    if not extra_cube :
                        # exchange letters
                        extra_cube = exchange_letters(l_candidate.encode('utf-8'), combinazione_candidate, free_cubes_candidate)
                        #strangers_in_the_night = free_cubes_candidate.self_simple_string_presentation()
                        #print 'exchange_letters'
                        if extra_cube and len(extra_cube.letters) != 6 :
                            '''
                            f = open('suspense.txt', 'w')
                            f.write(letter + '\n')
                            f.write(cube_t_s + '\n')
                            f.write(' '.join(cube_t.letters) + '\n')
                            f.write('Something special \n')
                            f.close()
                            '''
                            raise Exception("wrong number of letters! after exchange_letters")
                        if not extra_cube :
                            # replace not base
                            extra_cube = free_cubes_candidate.replace_not_base(l_candidate.encode('utf-8'))
                            if extra_cube and len(extra_cube.letters) != 6 :
                                raise Exception("wrong number of letters! after free_cubes_candidate.replace_not_base")
                            if not extra_cube :
                                # replace not base in used and exchange
                                extra_cube = replace_not_base_and_exchange(l_candidate.encode('utf-8'), combinazione_candidate, free_cubes_candidate)
                                if extra_cube and len(extra_cube.letters) != 6 :
                                    raise Exception("wrong number of letters! after replace_not_base_and_exchange")
                    if extra_cube :
                        combinazione_candidate.append(extra_cube)
                    else :
                        print '============================= Achtung!!! ============================='
                        f = open('ZZTOP.txt', 'w')
                        f.write(word.encode('utf-8') + '\n')
                        #f.write(free_cubes_candidate.self_string_presentation('we are the chempions!') + '\n')
                        f.write('free cubes candidates quantity : ' + str(len(free_cubes_candidate.cubes)) + '\n')
                        f.write('free cubes quantity : ' + str(len(free_cubes.cubes)) + '\n')
                        f.write('current word index : ' + str(wi) + '\n')
                        f.write('starting word index : ' + str(word_index) + '\n')
                        f.write('letter candidate : ' + l_candidate.encode('utf-8') + '\n')
                        f.close()
                        free_cubes.get_back(combinazione) #restore combination 
                        return None, None

                if len(combinazione_candidate) == len(word) :
                    free_cubes.get_back(combinazione)
                    combinazione_healthe(combinazione_candidate, ' FINAL RETURN comb candidate ')
                    free_cubes_candidate.get_back(combinazione_candidate) #needed to return full combination candidate!!!
                    free_cubes_candidate.self_letters_healthe()
                    if len(free_cubes_candidate.cubes) != 8:
                        raise Exception('>>>REDUNDANT CUBES DISCOVERED')
                    return  None, free_cubes_candidate # whole word was processed

        word_index += 1

    '''
    if len(combinazione) == len(word) :
        check_file.write(word.encode('utf-8') + '\n')
        ordered_letters = ''
        combinazione_candidate = copy.deepcopy(combinazione)
        for letter in word :
            for ordered_cube in combinazione_candidate :
                if letter.encode('utf-8') == ordered_cube.selected_letter :
                    ordered_letters += str(ordered_cube.id) + ' '
                    combinazione_candidate.remove(ordered_cube)
                    break
        check_file.write(ordered_letters + '\n')
        check_file.write('------------------------- \n')
    '''

    free_cubes.get_back(combinazione)
    if len(combinazione) == len(word) :
        return word, None

def collect_words(comb, file_lines):
    found_words = 0
    combs = []
    combs_string = []
    f = open('check_cubes\\' + comb.self_simple_string_presentation('file name comb') + '.txt', 'w')
    f.write(comb.self_string_presentation('file name comb') + '\n')
    for line in file_lines:
        zztop, alt_comb = collect_word2(line.rstrip(), comb, f)
        if alt_comb :
            asp = alt_comb.self_simple_string_presentation(comb.self_simple_string_presentation('father comb'))
            if asp not in combs_string :
                combs.append(alt_comb)
                combs_string.append(asp)
                #f.write(alt_comb.self_string_presentation('file alt comb') + '\n')
        else:
            if zztop :
                found_words += 1
                #f.write(line.rstrip() + '\n')
    #f.write(str(found_words))
    f.close()
    return found_words, combs

def loop_dict2(file_name, s_ind, in_q, out_q, mutex):

    file_lines = []
    mutex.acquire()
    f = open(file_name)
    for line in f :
        file_lines.append(line)
    f.close()
    print 'Initialized searcher : ', str(s_ind)
    mutex.release()

    while True :
        try :
            jm = in_q.get(0)
            #print 'Something got'
            if jm.status == 'jobjob' :
                #print ' jobjob was detected'
                combs = jm.combinations
                max = jm.max

                found = False
                break_s = False
                for comb in combs :
                    covered, ccombs = collect_words(comb, file_lines)
                    if not in_q.empty() :
                        jm = in_q.get(0)
                        if jm.status == 'BREAK' :
                            break_s = True
                            break
                        else :
                            print 'Unexpected message here, status : ', jm.status
                            raise

                    if covered > max :
                        found = True
                        out_q.put(job_message('MAX', covered, ccombs, comb, str(s_ind)))
                        break

                if not found and not break_s:
                    out_q.put(job_message('NO_SESSO', None, None))
            if jm.status == 'finito' :
                break
        except Queue.Empty:
            pass

def numeric_compare(x, y):
    sort_map = {'а':1, 'б':2, 'в':3, 'г':4, 'д':5, 'е':6, 'ё':7, 'ж':8, 'з':9, 'и':10, 'й':11, 'к':12, 'л':13, 'м':14, 
    'н':15, 'о':16, 'п':17, 'р':18, 'с':19, 'т':20, 'у':21, 'ф':22, 'х':23, 'ц':24, 'ч':25, 'ш':26, 'щ':27, 'ъ':28, 'ы':29, 'ь':30, 'э':31, 'ю':32, 'я':33}
    val_tor = sort_map[x.letter] - sort_map[y.letter]
    return val_tor 

def numeric_cubes_compare(x, y):
    val_tor = x.id - y.id
    return val_tor 
