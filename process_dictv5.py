import copy
from datetime import datetime
import os
import multiprocessing
import Queue

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

'''
cb1 = Cube(1, {'г' : True, 'б' : True, 'д': True, 'е' : True, 'к' : True, 'л' : False})  
cb2 = Cube(2, {'г' : False, 'л' : True, 'й' : True, 'о' : True, 'м' : True, 'щ' : True})  
cb3 = Cube(3, {'с' : True, 'р' : True, 'у' : True, 'т' : True, 'х' : True, 'ф' : True}) 
cb4 = Cube(4, {'к' : False, 'т' : False, 'ш' : True, 'ы' : True, 'ъ' : True, 'э' : True})
cb5 = Cube(5, {'ё' : True, 'в' : True, 'ж' : True, 'з' : True, 'п' : True, 'ч' : True})
cb6 = Cube(6, {'а' : False, 'е' : False, 'и' : True, 'ц' : True, 'я' : True, 'ю' : True})  
cb7 = Cube(7, {'а' : True, 'и' : False, 'о' : False, 'м' : False, 'н' : False, 'ь' : True})
cb8 = Cube(8, {'о' : False, 'н' : True, 'р' : False, 'у' : False, 'х' : False, 'ф' : False})
'''


cb1 = Cube(1, {'в' : False, 'г' : True,  'а' : False, 'к' : True,  'п' : True,  'т' : False})  
cb2 = Cube(2, {'к' : False, 'й' : True,  'м' : True,  'ц' : True,  'щ' : True,  'ь' : True})  
cb3 = Cube(3, {'л' : False, 'н' : True,  'р' : True,  'т' : True,  'х' : True,  'ф' : True})  
cb4 = Cube(4, {'а' : True,  'и' : False, 'о' : True,  'ф' : False, 'ы' : True,  'ъ' : True})  
cb5 = Cube(5, {'в' : True,  'б' : True,  'з' : True,  'п' : False, 'н' : False, 'с' : False})  
cb6 = Cube(6, {'ё' : True,  'е' : True,  'и' : True,  'о' : False, 'у' : True,  'ю' : True})  
cb7 = Cube(7, {'а' : False, 'ж' : True,  'е' : False, 'о' : False, 'э' : True,  'я' : True})  
cb8 = Cube(8, {'д' : True,  'л' : True,  'с' : True,  'р' : False, 'ч' : True,  'ш' : True})

'''
cb1 = Cube(1, {'д' : True, 'к' : True, 'л' : False, 'о' : True, 'у' : False, 'т' : False})  
cb2 = Cube(2, {'к' : False, 'й' : True, 'м' : True, 'ц' : True, 'щ' : True, 'ь' : True})  
cb3 = Cube(3, {'н' : True, 'р' : True, 'т' : True, 'ф' : True, 'ч' : True, 'ш' : True})  
cb4 = Cube(4, {'а' : False, 'е' : True, 'о' : False, 'ы' : True, 'ъ' : True, 'э' : True})  
cb5 = Cube(5, {'в' : True, 'г' : True, 'а' : True, 'н' : False, 'с' : False, 'х' : True})  
cb6 = Cube(6, {'а' : False, 'и' : True, 'п' : True, 'у' : True, 'ф' : False, 'ю' : True})  
cb7 = Cube(7, {'ё' : True, 'б' : True, 'е' : False, 'и' : False, 'о' : False, 'я' : True})  
cb8 = Cube(8, {'ж' : True, 'з' : True, 'л' : True, 'м' : False, 'с' : True, 'р' : False})
'''

'''
'а' 'б' 'в' 'г' 'д' 'е' 'ё' 'ж' 'з' 'и' 'й' 'к' 'л' 'м' 
'н' 'о' 'п' 'р' 'с' 'т' 'у' 'ф' 'х' 'ц' 'ч' 'ш' 'щ' 'ъ' 'ы' 'ь' 'э' 'ю' 'я'
'''
 
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

def collect_word2(word, free_cubes) :
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

    free_cubes.get_back(combinazione)
    if len(combinazione) == len(word) :
        return word, None

def collect_words(comb, file_name):
    found_words = 0
    combs = []
    combs_string = []
    for line in open(file_name):
        zztop, alt_comb = collect_word2(line.rstrip(), comb)
        if alt_comb :
            asp = alt_comb.self_simple_string_presentation(comb.self_simple_string_presentation('father comb'))
            if asp not in combs_string :
                combs.append(alt_comb)
                combs_string.append(asp)
        else:
            if zztop :
                found_words += 1

    return found_words, combs

def loop_dict2(file_name, s_ind, in_q, out_q):

    print 'Initialized searcher : ', str(s_ind)

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
                    covered, ccombs = collect_words(comb, file_name)
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
            
        except Queue.Empty:
            pass



sort_map = {'а':1, 'б':2, 'в':3, 'г':4, 'д':5, 'е':6, 'ё':7, 'ж':8, 'з':9, 'и':10, 'й':11, 'к':12, 'л':13, 'м':14, 
'н':15, 'о':16, 'п':17, 'р':18, 'с':19, 'т':20, 'у':21, 'ф':22, 'х':23, 'ц':24, 'ч':25, 'ш':26, 'щ':27, 'ъ':28, 'ы':29, 'ь':30, 'э':31, 'ю':32, 'я':33}

def numeric_compare(x, y):
    val_tor = sort_map[x.letter] - sort_map[y.letter]
    return val_tor 

def numeric_cubes_compare(x, y):
    val_tor = x.id - y.id
    return val_tor 

class job_message(object):
    def __init__(self, status, max, combinations, current_combination = None, searcher_ind = None):
        self.status = status
        self.max = max
        self.combinations = combinations
        self.current_combination = current_combination
        self.searcher_ind = searcher_ind

def main():
    print 'Dict talk'
    #####################
    # Test block
    '''
    cb11 = Cube(1, {'a' : True, 'b' : True, 'c' : True})
    cb11.selected_letter = 'a'
    cb21 = Cube(2, {'d' : True, 'e' : True, 'f' : True})
    cb21.selected_letter = 'e'

    cb31 = Cube(3, {'w' : False, 'r' : True, 'e' : True})
    cb41 = Cube(4, {'j' : True, 'g' : True, 'h' : False})
    combination = [cb11, cb21]
    fr_c = Free_Cubes([cb31, cb41])
    print fr_c.self_string_presentation()

    cb = painless_replacement('d', combination, fr_c)
    if cb :
        print cb.letters, ' selected letter: ', cb.selected_letter
    print '-----------------'
    print 'cb11.letters : ', cb11.letters, ' selected letter: ', cb11.selected_letter
    print 'cb21.letters : ', cb21.letters, ' selected letter: ', cb21.selected_letter
    print 'cb31.letters : ', cb31.letters
    print 'cb41.letters : ', cb41.letters
    print len(fr_c.cubes),'-',len(combination)
    '''
    #####################
    '''
    f = open('ZZTOP.txt', 'w')
    f.close()
    '''

    #loop_dict2('ororov3.txt')

    number_of_processors = int(os.environ["NUMBER_OF_PROCESSORS"]) - 1
    #number_of_processors = 1
    processes = []
    in_qs = []
    out_qs = []

    # init first combination to start searching
    fr_c = Free_Cubes([cb1, cb2, cb3, cb4, cb5, cb6, cb7, cb8])
    combs = [fr_c]
    max = 0
    duty_today = 'orfoggg_fwords_super.txt'

    for i in range(number_of_processors) :
        in_q = multiprocessing.Queue()
        out_q = multiprocessing.Queue()
        p = multiprocessing.Process(target=loop_dict2, args=(duty_today, i, in_q, out_q))
        processes.append(p)
        p.start()
        in_qs.append(in_q)
        out_qs.append(out_q)

    while len(combs) > 0 :
        job_portion = len(combs) / number_of_processors
        job_index = 0
        counter_of_tasks = 0
        if job_portion :
            for iq in in_qs :
                if (len(combs) - job_index) >= job_portion :
                    iq.put(job_message('jobjob', max, combs[job_index:(job_index+job_portion)]))
                    print job_index , ' : ', job_index+job_portion
                    job_index += job_portion + 1
                else :
                    iq.put(job_message('jobjob', max, combs[(job_index):]))
                    print (job_index), ':'
                counter_of_tasks += 1
        else :
            in_qs[0].put(job_message('jobjob', max, combs))
            counter_of_tasks += 1

        print 'counter_of_tasks : ', counter_of_tasks
        
        no_sesso = 0
        max_found = False
        while not max_found and counter_of_tasks != no_sesso:
            # read from output queuses max values
            for oq in out_qs :
                try :
                    response = oq.get(0)
                    if response.status == 'MAX' :
                        if max < response.max:
                            combs = response.combinations
                            max = response.max
                            comb = response.current_combination
                            print 'Fresh max : ', max, ' for searcher : ', response.searcher_ind
                            ###
                            f = open('champions.txt', 'a')
                            comb_current_max_str = comb.self_string_presentation('we are the champions!')
                            f.write(comb_current_max_str + ' - ' + str(max) + '  time: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
                            f.close()
                            ###
                            for iq in in_qs :
                                iq.put(job_message('BREAK',None,None))
                            max_found = True
                            break
                        else :
                            print 'Got the old MAX value!!!'
                    else :
                        if response.status == 'NO_SESSO' :
                            no_sesso += 1
                except Queue.Empty:
                    pass

        if counter_of_tasks == no_sesso :
            print 'This approach expired all found combinations, buy'
            print 'counter_of_tasks : ', counter_of_tasks, ' no sesso : ', no_sesso
            break

if __name__ == "__main__":
    main()
