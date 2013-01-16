# encoding: utf-8
import re


lines_dyn = [line.decode('utf8').strip() for line in open('chukovskiy_barto.txt')]
parolas = []

sort_map = {'а':'A', 'б':'B', 'в':'C', 'г':'D', 'д':'E', 'е':'F', 'ё':'G', 'ж':'H', 'з':'I', 'и':'J', 'й':'K', 'к':'L', 'л':'M', 'м':'N', 
'н':'O', 'о':'P', 'п':'Q', 'р':'R', 'с':'S', 'т':'T', 'у':'U', 'ф':'V', 'х':'W', 'ц':'X', 'ч':'Y', 'ш':'Z', 'щ':'z', 'ъ':'y', 'ы':'x', 'ь':'w', 'э':'v', 'ю':'u', 'я':'t'}

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

fs = open('processed.txt', 'w')
s_parolas = []

for line_d in lines_dyn:

    parolas = re.compile('[\w\s!.,:«»\-—;@\?()i"…]+').split(line_d)

    for parola in parolas :
        #print 'olololo'
        if 1 < len(parola) <= 8 and not parola in s_parolas :
            s_parolas.append(parola)
            fs.write(parola.encode('utf8') + '\n')

fs.close()
