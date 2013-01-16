import re

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
