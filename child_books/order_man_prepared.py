# encoding: utf-8
import re
import copy

lines_dyn = [line.decode('utf8').strip() for line in open('processed_m_m.txt')]
parolas = []

sort_map = {'а':'A', 'б':'B', 'в':'C', 'г':'D', 'д':'E', 'е':'F', 'ё':'G', 'ж':'H', 'з':'I', 'и':'J', 'й':'K', 'к':'L', 'л':'M', 'м':'N', 
'н':'O', 'о':'P', 'п':'Q', 'р':'R', 'с':'S', 'т':'T', 'у':'U', 'ф':'V', 'х':'W', 'ц':'X', 'ч':'Y', 'ш':'Z', 'щ':'z', 'ъ':'y', 'ы':'x', 'ь':'w', 'э':'v', 'ю':'u', 'я':'t'}

def convert_nai(stc) :
    ls = ''
    for l in stc:
        ls += sort_map[l.encode('utf8')]
        #print ls
    return ls

'''
out_s = ''

for line_d in lines_dyn:
    #parolas.extend(re.compile("[^а-яА-Я]").split(line_d))
    for lc in line_d:
        if lc not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.decode('utf8'):
            if lc not in out_s:
                out_s += lc

fs = open('processed.txt', 'w')
fs.write(out_s.encode('utf8') + '\n')
fs.close()
'''

#parolas = re.compile('[\w\s!.,:«»\-—;@\?()i"…\*]+').split(u'11ррррр@ррр 222рррр33 3ллл')

s_parolas = []

for parola in lines_dyn:
        #print 'olololo'
        if 1 < len(parola) <= 8 and not parola in s_parolas :
            s_parolas.append(parola)


fs = open('processed_m_m.txt', 'w')

stable_parolas = copy.deepcopy(s_parolas)
lines_super = []
indd = 0

for line_d in s_parolas:
    super = True
    ii = 0
    for line_s in stable_parolas:
        ii += 1
        #print ii
        if convert_nai(line_d) in convert_nai(line_s) and len(line_s) != len(line_d):
            super = False
            break
    indd += 1
    print indd
    if super :
        lines_super.append(line_d)
        fs.write(line_d.encode('utf8') + '\n')


fs.close()
