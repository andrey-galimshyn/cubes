import copy
from datetime import datetime
import os
import multiprocessing
import Queue

from search_process import Cube
from search_process import Free_Cubes
from search_process import loop_dict2
from search_process import job_message

def main():
    print 'Dict talk'

    '''
    cb1 = Cube(1, {'в' : False, 'г' : True,  'а' : False, 'к' : True,  'п' : True,  'т' : False,})
    cb2 = Cube(2, {'к' : False, 'й' : True,  'м' : True,  'ц' : True,  'щ' : True,  'ь' : True,})
    cb3 = Cube(3, {'л' : False, 'н' : True,  'р' : True,  'т' : True,  'х' : True,  'ф' : True,})
    cb4 = Cube(4, {'е' : True,  'и' : False, 'о' : True,  'ф' : False, 'ы' : True,  'ъ' : True,}) 
    cb5 = Cube(5, {'в' : True,  'б' : True,  'з' : True,  'п' : False, 'н' : False, 'с' : False,}) 
    cb6 = Cube(6, {'ё' : True,  'а' : True,  'и' : True,  'о' : False, 'у' : True,  'ю' : True,})
    cb7 = Cube(7, {'а' : False, 'ж' : True,  'е' : False, 'о' : False, 'э' : True,  'я' : True,})  
    cb8 = Cube(8, {'д' : True,  'л' : True,  'с' : True,  'р' : False, 'ч' : True,  'ш' : True,})
    '''

    '''
    cb1 = Cube(1, {'в' : False, 'г' : True, 'б' : True, 'п' : True, 'м' : True, 'т' : False,})  
    cb2 = Cube(2, {'к' : False, 'л' : False, 'й' : True, 'ц' : True, 'щ' : True, 'ь' : True,})  
    cb3 = Cube(3, {'з' : True, 'н' : True, 'р' : True, 'т' : True, 'х' : True, 'ш': True,})  
    cb4 = Cube(4, {'а' : True, 'ж' : True, 'е' : False, 'о' : True, 'ъ' : True, 'я' : True,})  
    cb5 = Cube(5, {'д' : True, 'к' : True, 'н' : False, 'с' : False, 'т' : False, 'ф' : True,})  
    cb6 = Cube(6, {'ё' : True, 'е' : True, 'и' : True, 'о' : False, 'у' : True, 'ю' : True,})  
    cb7 = Cube(7, {'а' : False, 'и' : False, 'о' : False, 'ф' : False, 'ы' : True, 'э' : True,})  
    cb8 = Cube(8, {'в' : True, 'а' : False, 'л' : True, 'с' : True, 'р' : False, 'ч' : True,})

    '''
    cb1 = Cube(1, {'в' : False, 'г' : True, 'б' : True, 'п' : True, 'м' : True, 'т' : False,})  
    cb2 = Cube(2, {'к' : False, 'й' : True, 'с' : False, 'ц' : True, 'щ' : True, 'ь' : True,})  
    cb3 = Cube(3, {'з' : True, 'н' : True, 'р' : True, 'т' : True, 'х' : True, 'ш' : True,})  
    cb4 = Cube(4, {'а' : True, 'ж' : True, 'е' : False, 'о' : True, 'ъ' : True, 'я' : True,})  
    cb5 = Cube(5, {'д' : True, 'к' : True, 'л' : False, 'н' : False, 'т' : False, 'ф' : True,})  
    cb6 = Cube(6, {'ё' : True, 'е' : True, 'и' : True, 'о' : False, 'у' : True, 'ю' : True,})  
    cb7 = Cube(7, {'а' : False, 'и' : False, 'о' : False, 'ф' : False, 'ы' : True, 'э' : True,})  
    cb8 = Cube(8, {'в' : True, 'а' : False, 'л' : True, 'с' : True, 'р' : False, 'ч' : True,})

    '''
    'а' 'б' 'в' 'г' 'д' 'е' 'ё' 'ж' 'з' 'и' 'й' 'к' 'л' 'м' 
    'н' 'о' 'п' 'р' 'с' 'т' 'у' 'ф' 'х' 'ц' 'ч' 'ш' 'щ' 'ъ' 'ы' 'ь' 'э' 'ю' 'я'
    '''




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
    #duty_today = 'orfoggg_fwords_super.txt'
    duty_today = 'child_books\\processed_m_m.txt'

    mutex = multiprocessing.Lock()
    for i in range(number_of_processors) :
        in_q = multiprocessing.Queue()
        out_q = multiprocessing.Queue()
        p = multiprocessing.Process(target=loop_dict2, args=(duty_today, i, in_q, out_q, mutex))
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
                    iq.put(job_message('jobjob', max, copy.deepcopy(combs[job_index:(job_index+job_portion)])))
                    print job_index , ' : ', job_index+job_portion
                    job_index += job_portion + 1
                else :
                    iq.put(job_message('jobjob', max, copy.deepcopy(combs[(job_index):])))
                    print (job_index), ':'
                counter_of_tasks += 1
        else :
            in_qs[0].put(job_message('jobjob', max, copy.deepcopy(combs)))
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
            for iq in in_qs :
                iq.put(job_message('finito', None, None))
            break

if __name__ == "__main__":
    main()
