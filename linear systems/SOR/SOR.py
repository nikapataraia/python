from cmath import inf, pi
import numpy as np


# -------------- 3 --------------------
def calSOR(n,matr,bientries,xientries,tolerance,maximumit,wO):
    if(tolerance < 0):
        tolerance = - tolerance
    def ite(v,w):
        # ??????????????????????
        elements = []
        for el in v:
            elements.append(el)


        
        def calcinw(ind):
            result = bientries[ind]
            for indx in range(n):
                if(indx!=ind):
                    result = result - matr[ind][indx] * elements[indx]
            return result/matr[ind][ind]

        for ind in range(n):
            elements[ind] = elements[ind] * (1-w) + w * calcinw(ind)
        return elements

    def tol(pre,new):
        mat = np.array(pre) - np.array(new)
        return np.linalg.norm(mat,inf) <= tolerance

    prev = xientries
    res = []
    for rn in range(maximumit):
        res = ite(prev,wO)
        if(tol(prev,res)):
            return res
        prev = res
    return None

# ----------- 2 -------------------
# print(calSOR(3,[[10.0, -1.1,0.0] , [ -1.0, 10.0, -2.0] ,[0.0,-2.0,10.0]] , [9.0,7.0,6.0] , [0.0,0.0,0.0] , 0.001, 100, 1.2)) 


# ----------- 4 ----------------
b = []
A = []
x = []
for ind in range(1,81):
    k = []
    for indr in range(1,81):
        k.append(0.0)
        x.append(0.0)
    A.append(k)
    

for i in range(80):
    b.append(pi)
    for j in range(80):
        if(i == j):
            A[i][j] = 2.0 * (i+1)
        if(j == i+2 or j == i-2):
            A[i][j] = 0.5 * (i+1)
        if(j == i+4 or j == i-4):
            A[i][j] = 0.25 * (i+1)

# with w = 1 , x(i j) = 0, maxIT = 1000
print(calSOR(80,A,b,x,0.00001,1000,1))





