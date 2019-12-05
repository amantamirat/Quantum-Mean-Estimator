'''
Created on Nov 21, 2019

@author: amanuel
'''
from math import cos, sin

def vec(angle):
    return [cos(angle / 2), sin(angle / 2)];

def kronVec(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            c += [a[i] * b[j]]
    return c

def toVectors(v):
    V = []
    for u in v:
        x = [1];
        for t in u:
            x = kronVec(x, vec(t))
        V.append(x)
    return V


def calc_mean(v):
    n = len(v)
    d = len(v[0])
    m = [0] * d
    for u in v:
        for i in range(0, d):
            m[i] = m[i] + u[i]
    for i in range(d):
        m[i] = m[i] / n
    return m