from cmath import inf
import numpy as np



def jacobi(n,mat,b,x,tol,maxIT):
    def tole(pre,new):
        vec = np.array(pre) - np.array(new)
        return np.linalg.norm(vec,inf) <= tol
    def ite(pr):
        prev = []
        elements = []
        for el in pr:
            prev.append(el)
            elements.append(el)
        def calc(ind):
            res = b[ind]
            for indx in range(n):
                if(ind != indx):
                    res = res - mat[ind][indx] * prev[indx]
            return res/mat[ind][ind]
        for ind in range(n):
            elements[ind] = calc(ind)
            print(ind + 1)
            print(elements[ind])
        return elements
    prev = []
    for el in x:
        prev.append(el)
    res = []
    for t in range(maxIT):
        res = ite(prev)
        if(tole(prev,res)):
            return (list(map(lambda x : round(x) , res)),t)
        prev = res
    return None
