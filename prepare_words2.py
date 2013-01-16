'''
accepted_list = []

empty_line = 1
first_line = 1




f = open('orfoggg_fwords.txt', 'w')
written = ''
counter = 0
for line in open('orfoggg.txt'):
    if line.rstrip() == '':
        #print 'empty'
        empty_line = 1
        first_line = 1
    else:
        if first_line:
            first_line = 0
            zz = line.split(',')[0].rstrip().replace('?','')
            if len(zz) <= 16 and not ' ' in zz and not '-' in zz and not zz.decode('utf8').istitle():
                if written != zz:
                    f.write(zz + '\n')
                    written = zz
                    counter += 1
                    if zz == 'мама':
                        print 'gggfgfgfg'

print counter
'''

sort_map = {'а':'A', 'б':'B', 'в':'C', 'г':'D', 'д':'E', 'е':'F', 'ё':'G', 'ж':'H', 'з':'I', 'и':'J', 'й':'K', 'к':'L', 'л':'M', 'м':'N', 
'н':'O', 'о':'P', 'п':'Q', 'р':'R', 'с':'S', 'т':'T', 'у':'U', 'ф':'V', 'х':'W', 'ц':'X', 'ч':'Y', 'ш':'Z', 'щ':'z', 'ъ':'y', 'ы':'x', 'ь':'w', 'э':'v', 'ю':'u', 'я':'t'}

def convert_nai(stc) :
    ls = ''
    for l in stc:
        ls += sort_map[l.encode('utf8')]
        #print ls
    return ls

lines_stable = [line.decode('utf8').rstrip() for line in open('otest.txt')]
lines_dyn = [line.decode('utf8').rstrip() for line in open('otest.txt')]

lines_super = []
indd = 0

fs = open('orfoggg_fwords_super.txt', 'w')

for line_d in lines_dyn:
    super = True
    ii = 0
    for line_s in lines_stable:
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
print 'list len : ', len(lines_super)