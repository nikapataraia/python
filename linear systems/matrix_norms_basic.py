from math import inf, sqrt
from random import random
from numpy import linalg as LA

x = int(input())
matrix = []
for ind in range(x):
    y = input()
    tempar = y.split(' ')
    if(len(tempar) > x):
        tempar = tempar[:x]
    tempar = list(map(lambda x : float(x),tempar))
    matrix.append(tempar)

def onenorm():
    max = -inf
    for el in matrix:
        Sum = sum(el)
        if(Sum > max):
            max = Sum
    return max

def infnorm():
    max = -inf
    for ind in range(len(matrix)):
        res = 0
        for el in matrix:
            res = res + el[ind]
        if(res > max):
            max = res
    return max

def frobe():
    res = 0
    for el in matrix:
        for elem in el:
            res = elem**2
    return sqrt(res)

def twonorm():
    return LA.norm(matrix,None)


print(str(round(onenorm())) + " " + str(round(twonorm())) + " " + str(round(infnorm())) + " "+ str(round(frobe())))
