from cmath import inf
import numpy as np

def custom_dot_mat(a , b):
    res = []
    for ind in range(len(a)):
        row = []
        for inde in range(len(b[0])):
            row.append(0)
        res.append(row)
    for ind in range(len(a)):
        for inde in range(len(b[0])):
            for elind in range(len(b)):
                res[ind][inde] += a[ind][elind] * b[elind][inde]
    return res

def custom_dot_vec(a,b):
    res = []
    for ind in range(len(a)):
        res.append(0)
    for ind in range(len(a)):
        for inde in range(len(a[ind])):
            res[ind] += a[ind][inde] * b[inde]
    return res
    
def richardson(n , a ,b , x,tol,maxIT,p,t):
    prev = x
    new = x
    p_inv = np.linalg.inv(p)
    # dot_pin_a = np.dot(np.array(p_inv), np.array(a))
    dot_pin_a = custom_dot_mat(p_inv , a)
    dot_ping_b = np.array(custom_dot_vec(p_inv , b) )* t
    # dot_ping_b = np.dot(np.array(p_inv) , b)  * t
    i  = np.identity(n)
    def tole(pre , ne):
        mat = np.array(pre) - np.array(ne)
        return np.linalg.norm(mat,inf) <= tol
    def ite(v):
        matp = i - t * dot_pin_a
        return np.dot(matp , v) + dot_ping_b
    for rn in range(maxIT):
        new = ite(prev)
        if(tole(new,prev)):
            print(new)
            return (list(map(lambda x : round(x) , new)),rn)
        prev = new
    return None