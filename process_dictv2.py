import copy


class Cube(object):
    def __init__(self, id, letters = {}, unconfirmed_letters = None):
        if len(letters) > 6:
            raise Exception('Too long list!')
        self.id = id
        self.letters = letters
        self.unconfirmed_letters = unconfirmed_letters

    def has(self,letter):
        if letter in self.letters:
            return True

    def has_not_base(self):
        for letter in self.letters :
            if not self.letters[letter] :
                return True

    def add_letter(self, letter):
        if len(self.letters) + len(self.unconfirmed_letters) == 6:
            raise Exception('Too long list!')
        if not letter in self.unconfirmed_letters:
            self.unconfirmed_letters[letter] = False # False because added letter is never base

    def confirm(self):
        if len(self.letters) + len(self.unconfirmed_letters) > 6:
            raise Exception('Too long lists of confirmed and unconfirmed letters!')
        self.letters.update(self.unconfirmed_letters)
        self.unconfirmed_letters = {}

    def remove_unconfirmed(self):
        self.unconfirmed_letters = {}
    
    def replace_not_base(self, letter):
        for let in self.letters:
            if not self.letters[let] :
                del self.letters[let]
                self.unconfirmed_letters[letter] = False  # False because added letter is never base
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
                self.cubes[:] = [x for x in self.cubes if x.id != cube.id]
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

cb1 = Cube(1, {'а' : True, 'б' : True, 'в' : True, 'г' : True, 'д' : True, 'е' : True}, {})
cb2 = Cube(2, {'и' : True, 'й' : True, 'к' : True, 'л' : True, 'м' : True, 'н' : True}, {})
cb3 = Cube(3, {'р' : True, 'с' : True, 'т' : True, 'у' : True, 'ф' : True, 'х' : True}, {})
cb4 = Cube(4, {'ш' : True, 'щ' : True, 'ъ' : True, 'ы' : True, 'ь' : True, 'э' : True}, {})
cb5 = Cube(5, {'ё' : True, 'ж' : True, 'з' : True, 'о' : True, 'п' : True, 'ч' : True}, {})
cb6 = Cube(6, {'ю' : True, 'я' : True, 'ц' : True, 'г' : False, 'д' : False, 'е' : False}, {})
cb7 = Cube(7, {'и' : False, 'й' : False, 'к' : False, 'л' : False, 'м' : False, 'н' : False}, {})
cb8 = Cube(8, {'р' : False, 'с' : False, 'т' : False, 'у' : False, 'ф' : False, 'х' : False}, {})

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
                    extra_cube = free_cubes_candidate.get_by_letter(l_candidate.encode('utf-8'))
                    if not extra_cube :
                        extra_cube = free_cubes_candidate.replace_not_base_and_get(l_candidate.encode('utf-8'))
                    if extra_cube :
                        combinazione_candidate.append(extra_cube)
                if len(combinazione_candidate) == len(word) :
                    free_cubes_candidate.get_back(combinazione_candidate)
                    free_cubes_candidate.confirm()
                    bla = free_cubes_candidate.self_string_presentation(word)
                    if not bla in all_found :
                        all_found.append(bla)
                        combinazioni.append(free_cubes_candidate)
                        f = open('ZZZZZ2.txt', 'a')
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

    f = open('ZZZZZ2.txt', 'w')
    f.write('------------------------ BEGGGGIN---------------\n')
    f.close()
        
    f = open(file_name + '_words.txt', 'w')
    f.write('-----------BEGIN-----------------------------------\n')
    f.close()
    
    while True:
        if len(combinazioni) != 0:
            curr_combinazione = combinazioni[0]
            combinazioni.remove(curr_combinazione)
            print len(combinazioni)
            f = open(file_name + '_words.txt', 'a')
            for line in open(file_name):
                zztop = collect_word(line.rstrip(), curr_combinazione)
                if zztop:
                    f.write(zztop.encode('utf8') + '\n')
            f.write('----------------------------------------------\n')
            for frc in curr_combinazione.cubes :
                for frl in frc.letters :
                    f.write(frl)
                    f.write(' ')
                f.write('\n')
            f.write('***********************************************\n')
            f.close()

            
        else :
            break


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

    fr_c = Free_Cubes([cb1, cb2, cb3, cb4, cb5, cb6, cb7, cb8])
    '''
    frc = fr_c.get_empty()
    for frrrrr in fr_c.cubes :
        print '------- Confirmed letters : ', len(frrrrr.letters), ' ------------- Unconfirmed letters : ', len(frrrrr.unconfirmed_letters)
    print ' ================================= '
    frc.add_letter('ы')
    print '----- Free cubes health after adding of the letter ---------- '
    for frrrrr in fr_c.cubes :
        print '------- Confirmed letters : ', len(frrrrr.letters), ' ------------- Unconfirmed letters : ', len(frrrrr.unconfirmed_letters)
    print ' ================================= '
    print '------- Confirmed letters : ', len(frc.letters), ' ------------- Unconfirmed letters : ', len(frc.unconfirmed_letters)
    print ' ================================= '
    print '----- Free cubes health after GETBACK of the letter ---------- '
    fr_c.get_back([frc])
    for frrrrr in fr_c.cubes :
        print '------- Confirmed letters : ', len(frrrrr.letters), ' ------------- Unconfirmed letters : ', len(frrrrr.unconfirmed_letters)
    print ' ================================= '
    print '----- Free cubes health after CONFIRM of the letter ---------- '
    fr_c.confirm()
    for frrrrr in fr_c.cubes :
        print '------- Confirmed letters : ', len(frrrrr.letters), ' ------------- Unconfirmed letters : ', len(frrrrr.unconfirmed_letters)
    print ' ================================= '
    print ' ============ TIME TO REPLACE NOT BASE ===================== '
    jok = fr_c.self_string_presentation()
    f = open('ZZZZZ.txt', 'w')
    f.write(jok + '\n')
    extra_cube = fr_c.replace_not_base_and_get('э')
    fr_c.get_back([extra_cube])
    fr_c.confirm()
    print ' ============ Free cubes health after REPLACE NOT BASE of the letter ===================== '
    for frrrrr in fr_c.cubes :
        print '------- Confirmed letters : ', len(frrrrr.letters), ' ------------- Unconfirmed letters : ', len(frrrrr.unconfirmed_letters)
    print ' ================================= '
    jok = fr_c.self_string_presentation()
    f = open('ZZZZZ.txt', 'a')
    f.write(jok + '\n')
    '''


    #####################
    loop_dict('ororov2.txt')
    #loop_dict('orfoggg_fwords.txt')

if __name__ == "__main__":
    main()
