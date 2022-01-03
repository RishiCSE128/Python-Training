import matplotlib.pyplot as plt
import numpy as np
import time 
import matplotlib

font = {'size'   : 22}

matplotlib.rc('font', **font)

def list_insert_test():
    time_to_add_end = []
    time_to_add_beg = []

    # insert at end
    test_list = []
    print('Testing Insert at end... ')
    for _ in range(10**5):
        t = time.time()
        test_list.append('X')
        time_to_add_end.append(time.time() - t)

    # insert at begining
    test_list = []
    print('Testing Insert at begining...')
    for _ in range(10**5):
        t = time.time()
        test_list.insert(0, 'X')
        time_to_add_beg.append(time.time()- t)
    
    # plotting params 
    plt.plot(time_to_add_beg, 'r', 
        label=f'Insert at beg : Mean time taken {np.mean(time_to_add_beg)} sec.')
    plt.plot(time_to_add_end, 'b' ,
        label=f'Insert at end  : Mean time taken {np.mean(time_to_add_end)} sec.')

    plt.xlabel('Number of item(s) inserted')
    plt.ylabel('Time Taken')
    plt.suptitle('Python3 List insertion Benchmarking')
    plt.legend()
    plt.yscale('log')
    
    
    plt.show()
    
list_insert_test()