﻿import copy
from datetime import datetime

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
                ordered_letters = sorted(ordered_cube.letters)
            except KeyError:
                f = open('suspense.txt', 'w')
                f.write('------------------------ BEGGGGIN---------------\n')
                f.write(word.encode('utf8'))
                f.close()
                raise
            rs += ''.join(ordered_letters)
        return rs

cb1 = Cube(1, {'а' : True, 'б' : True, 'в' : True, 'г' : True, 'д' : True, 'е' : True})
cb2 = Cube(2, {'и' : True, 'й' : True, 'к' : True, 'л' : True, 'м' : True, 'н' : True})
cb3 = Cube(3, {'р' : True, 'с' : True, 'т' : True, 'у' : True, 'ф' : True, 'х' : True})
cb4 = Cube(4, {'ш' : True, 'щ' : True, 'ъ' : True, 'ы' : True, 'ь' : True, 'э' : True})
cb5 = Cube(5, {'ё' : True, 'ж' : True, 'з' : True, 'о' : True, 'п' : True, 'ч' : True})
cb6 = Cube(6, {'ю' : True, 'я' : True, 'ц' : True, 'г' : False, 'д' : False, 'е' : False})
cb7 = Cube(7, {'и' : False, 'й' : False, 'к' : False, 'л' : False, 'м' : False, 'н' : False})
cb8 = Cube(8, {'р' : False, 'с' : False, 'т' : False, 'у' : False, 'ф' : False, 'х' : False})

all_found = []
combinazioni = []

# If there are no cubes with desired letter
# we are searching for letter in selected cubes and 
# if this letter is not selected we may exchange letters
def exchange_letters(letter, collection, free_cubes) :
    for cube in collection :
        if letter != cube.selected_letter and cube.has(letter) :
            cube_t = free_cubes.cubes.pop()
            key, val = cube_t.letters.popitem()
            cube.letters.update({key : val})
            cube_t.letters[letter] = cube.letters[letter]
            del cube.letters[letter]
            return cube_t

def replace_not_base_and_exchange(letter, collection, free_cubes) :
    for cube in collection :
        if letter != cube.selected_letter :
            let_buy = cube.get_not_base() 
            if let_buy :
                cube_t = free_cubes.cubes.pop()
                key, val = cube_t.letters.popitem()
                cube.letters.update({key : val})
                cube_t.letters[letter] = False
                del cube.letters[let_buy]
                return cube_t

def collect_word(word, free_cubes) :
    if len(word) == 0:
        return None
    combinazione = []
    word=word.decode('utf-8')
    word_index = 0
    for l in word:
        lc = free_cubes.get_by_letter(l.encode('utf-8'))
        if lc :
            combinazione.append(lc)
        else :
            combinazione_candidate = copy.deepcopy(combinazione)
            free_cubes_candidate = copy.deepcopy(free_cubes)
            for l_candidate in word[word_index:] :
                extra_cube = free_cubes_candidate.get_by_letter(l_candidate.encode('utf-8'))
                if not extra_cube :
                    # exchange letters
                    extra_cube = exchange_letters(l_candidate.encode('utf-8'), combinazione_candidate, free_cubes_candidate)
                    if not extra_cube :
                        # replace not base
                        extra_cube = free_cubes_candidate.replace_not_base(l_candidate.encode('utf-8'))
                if extra_cube :
                    combinazione_candidate.append(extra_cube)
            if len(combinazione_candidate) == len(word) :
                free_cubes_candidate.get_back(combinazione_candidate)
                bla = free_cubes_candidate.self_string_presentation(word)
                if not bla in all_found :
                    all_found.append(bla)
                    combinazioni.append(free_cubes_candidate)
                    #f = open('ZZZZZ3.txt', 'a')
                    #f.write(bla + '\n')

                break # whole word was processed

        word_index += 1

    free_cubes.get_back(combinazione)
    if len(combinazione) == len(word) :
        return word

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
            combinazione_candidate = copy.deepcopy(combinazione)
            free_cubes_candidate = copy.deepcopy(free_cubes)
            for l_candidate in word[word_index:] :
                extra_cube = free_cubes_candidate.get_by_letter(l_candidate.encode('utf-8'))
                if not extra_cube :
                    # exchange letters
                    extra_cube = exchange_letters(l_candidate.encode('utf-8'), combinazione_candidate, free_cubes_candidate)
                    if not extra_cube :
                        # replace not base
                        extra_cube = free_cubes_candidate.replace_not_base(l_candidate.encode('utf-8'))
                        if not extra_cube :
                            # replace not base in used and exchange
                            extra_cube = replace_not_base_and_exchange(l_candidate, combinazione_candidate, free_cubes_candidate)
                if extra_cube :
                    combinazione_candidate.append(extra_cube)
            if len(combinazione_candidate) == len(word) :
                free_cubes_candidate.get_back(combinazione_candidate)
                return  None, free_cubes_candidate # whole word was processed

        word_index += 1

    free_cubes.get_back(combinazione)
    if len(combinazione) == len(word) :
        return word, None


def loop_dict(file_name):
    # init first combination to start searching
    fr_c = Free_Cubes([cb1, cb2, cb3, cb4, cb5, cb6, cb7, cb8])
    all_found.append(fr_c.self_string_presentation('wellcome to the New York!'))
    combinazioni.append(fr_c)

    '''
    f = open('ZZZZZ3.txt', 'w')
    f.write('------------------------ BEGGGGIN---------------\n')
    f.close()


    f = open(file_name + '_words.txt', 'w')
    f.write('-----------BEGIN-----------------------------------\n')
    f.close()
    '''

    f = open('champions.txt', 'w')
    f.write('-----------BEGIN-----------------------------------\n')
    f.close()

    found_words_champion = 0
    while True:
        if len(combinazioni) != 0:
            curr_combinazione = combinazioni[0]
            combinazioni.remove(curr_combinazione)
            found_words = 0
            for line in open(file_name):
                zztop = collect_word(line.rstrip(), curr_combinazione)
                if zztop:
                    found_words += 1
                    '''
                    f = open(file_name + '_words.txt', 'a')
                    f.write(zztop.encode('utf8') + '\n')
                    f.write('----------------------------------------------\n')
                    for frc in curr_combinazione.cubes :
                        for frl in frc.letters :
                            f.write(frl)
                            f.write(' ')
                        f.write('\n')
                    f.write('***********************************************\n')
                    f.close()
                    '''
            if found_words_champion < found_words :
                found_words_champion = found_words
                print found_words_champion
                f = open('champions.txt', 'a')
                f.write(curr_combinazione.self_string_presentation('we are the chempions!') + ' - ' + str(found_words_champion) + '\n')
                f.close()


        else :
            break

def collect_words(comb, file_name):
    found_words = 0
    combs = []
    for line in open(file_name):
        zztop, alt_comb = collect_word2(line.rstrip(), curr_combinazione)
        if alt_comb:
            combs.append(alt_comb)
        else:
            found_words += 1

    return found_words, combs

def loop_dict2(file_name):
    # init first combination to start searching
    fr_c = Free_Cubes([cb1, cb2, cb3, cb4, cb5, cb6, cb7, cb8])
    max = 0
    combs = [fr_c]
    ccombs = []
    while len(combs) > 0 :
        for comb in combs :
            covered, ccombs = collect_words(comb, file_name)
            if covered > max :
                max = covered
                ###
                f = open('champions.txt', 'a')
                f.write(comb.self_string_presentation('we are the chempions!') + ' - ' + str(found_words_champion) + '  time: ' + datetime.now() + '\n')
                f.close()
                ###
                break
        combs = ccombs
        ccombs = []



sort_map = {'а':1, 'б':2, 'в':3, 'г':4, 'д':5, 'е':6, 'ё':7, 'ж':8, 'з':9, 'и':10, 'й':11, 'к':12, 'л':13, 'м':14, 
'н':15, 'о':16, 'п':17, 'р':18, 'с':19, 'т':20, 'у':21, 'ф':22, 'х':23, 'ц':24, 'ч':25, 'ш':26, 'щ':27, 'ъ':28, 'ы':29, 'ь':30, 'э':31, 'ю':32, 'я':33}

def numeric_compare(x, y):
    val_tor = sort_map[x.letter] - sort_map[y.letter]
    return val_tor 

def numeric_cubes_compare(x, y):
    val_tor = x.id - y.id
    return val_tor 

def main():
    print 'Dict talk'
    #####################
    # Test block

    cb11 = Cube(1, {'a' : True, 'b' : True, 'c' : True})
    cb21 = Cube(2, {'d' : True, 'e' : True, 'f' : True})
    cb31 = Cube(3, {'w' : False, 'r' : True, 'k' : True})
    cb41 = Cube(4, {'j' : True, 'g' : True, 'h' : False})
    combination = [cb11, cb21]
    fr_c = Free_Cubes([cb31, cb41])
    cb = replace_not_base_and_exchange('X', combination, fr_c)
    if cb :
        print cb.letters
    print '-----------------'
    print 'cb11.letters : ', cb11.letters
    print 'cb21.letters : ', cb21.letters
    print 'cb31.letters : ', cb31.letters
    print 'cb41.letters : ', cb41.letters
    print len(fr_c.cubes),'-',len(combination)



    #####################
    #loop_dict('ororov3.txt')
    #loop_dict('orfoggg_fwords.txt')

if __name__ == "__main__":
    main()
