import copy


class L(object):
    def __init__(self, letter, base = True, confirmed = True):
        self.base = base
        self.confirmed = confirmed
        self.letter = letter
        self.in_word = False

    def __str__(self):
        return self.letter

class Cube(object):
    def __init__(self, id, letters = []):
        if len(letters) > 6:
            raise Exception('Too long list!')
        self.id = id
        self.letters = letters

    def has(self,letter):
        for l in self.letters:
            if l.letter == letter:
                return l

    def has_not_base(self):
        for l in self.letters:
            if not l.base :
                return l

    def add_letter(self, letter):
        if len(self.letters) == 6:
            raise Exception('Too long list!')
        self.letters.append(L(letter, False, False))

    def confirm(self):
        for let in self.letters:
            if not let.confirmed:
                let.confirmed = True

    def remove_unconfirmed(self):
        self.letters[:] = [x for x in self.letters if x.confirmed]
    
    def replace_not_base(self, letter):
        for let in self.letters:
            if not let.base:
                let.letter = letter
                return True

class Free_Cubes(object):
    def __init__(self, cubes = []):
        self.cubes = cubes

    def get_by_letter(self, letter):
       for cube in self.cubes:
            if cube.has(letter):
                self.cubes[:] = [x for x in self.cubes if x.id != cube.id]
                return cube

    def get_back(self, rcubes):
        self.cubes.extend(rcubes)

    def get_empty(self):
        for cube in self.cubes:
            if len(cube.letters) < 6:
                #print 'Getting empty: ', len(self.cubes)
                self.cubes[:] = [x for x in self.cubes if x.id != cube.id]
                #print 'Exclude goten empty cube: ', len(self.cubes)
                return cube

    def replace_not_base_and_get(self, letter_missing) :
        for cube in self.cubes:
            l = cube.has_not_base()
            if l :
                if cube.replace_not_base(letter_missing) :
                    self.cubes[:] = [x for x in self.cubes if x != cube]
                    return cube

    def confirm(self):
        for cb in self.cubes:
            cb.confirm()

    def remove_unconfirmed(self):
        for cb in self.cubes:
            cb.remove_unconfirmed()

    '''
    def compare(self, other_combination) :
        for self_cube in self.cubes :
            scl = sorted(self_cube.letters, cmp=numeric_compare)
            equality_found = False
            for other_cube in other_combination.cubes :
                ocl = sorted(other_cube.letters, cmp=numeric_compare)
                if len(ocl) == len(scl) and all(ocl[i].letter == scl[i].letter for i in range(len(scl)-1)):
                    equality_found = True
            if not equality_found :
                return False
        return True
    '''

    def self_string_presentation(self, word = 'jazz') :
        cubes_ordered = sorted(self.cubes, cmp=numeric_cubes_compare)
        rs = ''
        for ordered_cube in cubes_ordered :
            try:
                ordered_letters = sorted(ordered_cube.letters, cmp=numeric_compare)
            except KeyError:
                f = open('suspense.txt', 'w')
                f.write('------------------------ BEGGGGIN---------------\n')
                f.write(word.encode('utf8'))
                f.close()
                raise
            for orl in ordered_letters :
                rs += orl.letter
        return rs

cb1 = Cube(1, [L('а'), L('б'), L('в'), L('г'), L('д'), L('е')])
cb2 = Cube(2, [L('и'), L('й'), L('к'), L('л'), L('м'), L('н')])
cb3 = Cube(3, [L('р'), L('с'), L('т'), L('у'), L('ф'), L('х')])
cb4 = Cube(4, [L('ш'), L('щ'), L('ъ'), L('ы'), L('ь'), L('э')])
cb5 = Cube(5, [L('ё'), L('ж'), L('з'), L('о'), L('п'), L('ч')])
cb6 = Cube(6, [L('ю'), L('я'), L('ц')])
cb7 = Cube(7, [])
cb8 = Cube(8, [])

all_found = []
combinazioni = []

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
            frc = free_cubes.get_empty()
            if frc :
                frc.add_letter(l.encode('utf-8'))
                combinazione.append(frc)
            else :
                combinazione_candidate = copy.deepcopy(combinazione)
                free_cubes_candidate = copy.deepcopy(free_cubes)
                for l_candidate in word[word_index:] :
                    extra_cube = free_cubes_candidate.replace_not_base_and_get(l_candidate.encode('utf-8'))
                    if extra_cube :
                        combinazione_candidate.append(extra_cube)
                if len(combinazione_candidate) == len(word) :
                    free_cubes_candidate.get_back(combinazione_candidate)
                    bla = free_cubes_candidate.self_string_presentation(word)
                    if not bla in all_found :
                        all_found.append(bla)
                        combinazioni.append(free_cubes_candidate)
                        f = open('ZZZZZ.txt', 'a')
                        f.write(bla + '\n')

                break # whole word was processed

        word_index += 1

    free_cubes.get_back(combinazione)
    if len(combinazione) == len(word) :
        free_cubes.confirm()
        return word
    else:
        free_cubes.remove_unconfirmed()

def loop_dict(file_name):
    # init first combination to start searching
    fr_c = Free_Cubes([cb1, cb2, cb3, cb4, cb5, cb6, cb7, cb8])
    all_found.append(fr_c.self_string_presentation('wellcome to the New York!'))
    combinazioni.append(fr_c)

    f = open('ZZZZZ.txt', 'w')
    f.write('------------------------ BEGGGGIN---------------\n')
    f.close()
        
    f = open(file_name + '_words_old.txt', 'w')
    f.write('-----------BEGIN-----------------------------------\n')
    f.close()

    while True:
        if len(combinazioni) != 0:
            curr_combinazione = combinazioni[0]
            combinazioni.remove(curr_combinazione)
            print len(combinazioni)
            #f = open(file_name + '_words_old.txt', 'a')
            for line in open(file_name):
                zztop = collect_word(line.rstrip(), curr_combinazione)
                #if zztop:
                    #f.write(zztop.encode('utf8') + '\n')
            #f.write('----------------------------------------------\n')
            #for frc in curr_combinazione.cubes :
                #for frl in frc.letters :
                    #f.write(frl.letter)
                    #f.write(' ')
                #f.write('\n')
            #f.write('***********************************************\n')
            #f.close()

            
        else :
            break

    '''
    for c_p_c in combinazioni :
        f.write('==============================================\n')
        for c_p_l in c_p_c.cubes :
            for c_p_ll in c_p_l.letters :
                f.write(c_p_ll.letter)
                f.write(' ')
            f.write('\n')
    '''
    '''
    f.write('==============================================\n')
    new_free_cubes = copy.deepcopy(free_cubes)
    for frc in new_free_cubes.cubes :
        print frc.id, ' : ', len(frc.letters)
        for frl in frc.letters :
            f.write(frl.letter)
            f.write(' ')
        f.write('\n')
    '''

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
    loop_dict('ororov2.txt')
    #loop_dict('orfoggg_fwords.txt')

    '''
    data_to_sort = [L('я'), L('о'), L('ж')]
    print sort_map[data_to_sort[0].letter]
    ddd = sorted(data_to_sort, cmp=numeric_compare)
    print sort_map[ddd[0].letter]
    '''
    #####################
    '''
    cb1 = Cube(1, [L('z', False, True)])
    cb2 = Cube(2, [L('x', True, True)])
    free_cubes = Free_Cubes([cb1, cb2])
    jok = free_cubes.replace_not_base_and_get('j')
    print len(free_cubes.cubes)
    print 'jok.id: ', jok.id
    print 'jok.letetr: ', jok.letters[0].letter
    '''
    #####################

if __name__ == "__main__":
    main()
