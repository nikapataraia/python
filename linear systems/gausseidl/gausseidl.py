from cmath import inf
import numpy as np
def gausseidl(n,mat,b,x,tol,maxIT):
    def ite(v):
        elements = []
        for el in v:
            elements.append(el)
        def calcinw(ind):
            result = b[ind]
            for indx in range(n):
                if(indx!=ind):
                    result = result - mat[ind][indx] * elements[indx]
            return result/mat[ind][ind]

        for ind in range(n):
            elements[ind] = calcinw(ind)
            print(ind + 1)
            print(elements[ind])
        return elements

    def tole(pre,new):
        mat = np.array(pre) - np.array(new)
        return np.linalg.norm(mat,inf) <= tol

    prev = x
    res = []
    for rn in range(maxIT):
        res = ite(prev)
        if(tole(prev,res)):
            return (list(map(lambda x : round(x) , res)),rn)
        prev = res
    return None


