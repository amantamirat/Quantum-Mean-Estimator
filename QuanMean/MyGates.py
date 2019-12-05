'''
Created on Jan 11, 2019

@author: Aman
'''
from math import pi


def c3x(circuit, c1, c2, c3, target, u=pi):
    circuit.h(target)
    c3z(circuit, c1, c2, c3, target, u)
    circuit.h(target)

  
def c4x(circuit, c1, c2, c3, c4, target, u=pi):
    circuit.h(target)
    c4z(circuit, c1, c2, c3, c4, target, u)
    circuit.h(target)


def c5x(circuit, c1, c2, c3, c4, c5, target, u=pi):
    circuit.h(target)
    c5z(circuit, c1, c2, c3, c4, c5, target, u)
    circuit.h(target)


def c2z(circuit, c1, c2, target, u=pi):
    circuit.cu1(u / 2, c1, target)
    circuit.cx(c1, c2)
    circuit.cu1(-u / 2, c2, target)
    circuit.cx(c1, c2)
    circuit.cu1(u / 2, c1, target)


def c3z(circuit, c1, c2, c3, target, u=pi):
    circuit.cu1(u / 4, c1, target)
    circuit.cx(c1, c2)
    circuit.cu1(-u / 4, c2, target)
    circuit.cx(c1, c2)
    circuit.cu1(u / 4, c2, target)
    circuit.cx(c2, c3)
    circuit.cu1(-u / 4, c3, target)
    circuit.cx(c1, c3)
    circuit.cu1(u / 4, c3, target)
    circuit.cx(c2, c3)
    circuit.cu1(-u / 4, c3, target)
    circuit.cx(c1, c3)
    circuit.cu1(u / 4, c3, target)   


def c4z(circuit, c1, c2, c3, c4, target, u=pi):
    circuit.cu1(u / 2, c4, target)
    c3x(circuit, c1, c2, c3, c4)
    circuit.cu1(-u / 2, c4, target)
    c3x(circuit, c1, c2, c3, c4)
    c3z(circuit, c1, c2, c3, target, u / 2)


def c5z(circuit, c1, c2, c3, c4, c5, target, u=pi):
    circuit.cu1(u / 2, c5, target)
    c4x(circuit, c1, c2, c3, c4, c5)
    circuit.cu1(-u / 2, c5, target)
    c4x(circuit, c1, c2, c3, c4, c5)
    c4z(circuit, c1, c2, c3, c4, target, u / 2)


def cy(circuit, c1, target, u=pi):
    circuit.cu3(u, 0, 0, c1, target)


def c2y(circuit, c1, c2, target, u=pi):
    cy(circuit, c2, target, u / 2)
    circuit.cx(c1, c2)
    cy(circuit, c2, target, -u / 2)
    circuit.cx(c1, c2)
    cy(circuit, c1, target, u / 2)


def c3y(circuit, c1, c2, c3, target, u=pi):
    cy(circuit, c1, target, u / 4)
    circuit.cx(c1, c2)
    cy(circuit, c2, target, -u / 4)
    circuit.cx(c1, c2)
    cy(circuit, c2, target, u / 4)
    circuit.cx(c2, c3)
    cy(circuit, c3, target, -u / 4)
    circuit.cx(c1, c3)
    cy(circuit, c3, target, u / 4)
    circuit.cx(c2, c3)
    cy(circuit, c3, target, -u / 4)
    circuit.cx(c1, c3)
    cy(circuit, c3, target, u / 4) 


def c4y(circuit, c1, c2, c3, c4, target, u=pi):
    cy(circuit, c4, target, u / 2)
    c3x(circuit, c1, c2, c3, c4)
    cy(circuit, c4, target, -u / 2)
    c3x(circuit, c1, c2, c3, c4)
    c3y(circuit, c1, c2, c3, target, u / 2)


def c5y(circuit, c1, c2, c3, c4, c5, target, u=pi):
    cy(circuit, c5, target, u / 2)
    c4x(circuit, c1, c2, c3, c4, c5)
    cy(circuit, c5, target, -u / 2)
    c4x(circuit, c1, c2, c3, c4, c5)
    c4y(circuit, c1, c2, c3, c4, target, u / 2)


def n_controlled_x(circuit, qin, target):
    n = len(qin)
    if n == 1:
        circuit.cx(qin[0], target)
    elif n == 2:
        circuit.ccx(qin[0], qin[1], target)
    elif n == 3:
        c3x(circuit, qin[0], qin[1], qin[2], target)
    elif n == 4:
        c4x(circuit, qin[0], qin[1], qin[2], qin[3], target)
    elif n == 5:
        c5x(circuit, qin[0], qin[1], qin[2], qin[3], qin[4], target)
    else:
        raise('more than 5 controller is not implemented yet')


def n_rotate_y(circuit, fin, target, u):
    n = len(fin)
    if n == 1:
        cy(circuit, fin[0], target, u)
    elif n == 2:
        c2y(circuit, fin[0], fin[1], target, u)
    elif n == 3:
        c3y(circuit, fin[0], fin[1], fin[2], target, u)
    elif n == 4:
        c4y(circuit, fin[0], fin[1], fin[2], fin[3], target, u)
    elif n == 5:
        c5y(circuit, fin[0], fin[1], fin[2], fin[3], fin[4], target, u)
    else:
        raise('more than 5 controller is not implemented yet')


def n_rotate_z(circuit, fin, target, u=pi):
    n = len(fin)
    if n == 1:
        circuit.cu1(u, fin[0], target)
    elif n == 2:
        c2z(circuit, fin[0], fin[1], target, u)
    elif n == 3:
        c3z(circuit, fin[0], fin[1], fin[2], target, u)
    elif n == 4:
        c4z(circuit, fin[0], fin[1], fin[2], fin[3], target, u)
    elif n == 5:
        c5z(circuit, fin[0], fin[1], fin[2], fin[3], fin[4], target, u)
    else:
        raise('more than 5 controller is not implemented yet')

