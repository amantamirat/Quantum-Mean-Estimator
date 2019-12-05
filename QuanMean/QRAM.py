'''
Created on Nov 2, 2019

@author: amanuel
'''
from MyGates import n_rotate_y
get_bin = lambda x, n: format(x, 'b').zfill(n)


def load(circuit, qin, dat, av):
    M = len(av)
    n = len(qin)
    ds = len(dat)
    if(n > 5):
        raise('works for only less than 5 controllers') 
    for i in range(M):
        bn = get_bin(i, n)
        for j in range(n):
            if bn[(n - 1) - j] == '0':
                circuit.x(qin[j])
        for k in range(ds):
            n_rotate_y(circuit, qin, dat[k], av[i][ds - k - 1])
        for j in range(n):
            if bn[(n - 1) - j] == '0':
                circuit.x(qin[j])
