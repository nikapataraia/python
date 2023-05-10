import numpy as np 


def QR_fac(A):
    n = len(A)
    m = len(A[0])
    newA = []
    for ind in range(n):
        newA.append(np.array(list(map(lambda x : float(x) , A[ind]))))
    transp = np.array(newA).T
    Q = np.zeros((m,n))
    R = np.zeros((m,m))
    for ind in range(m):
        y = transp[ind]
        for inde in range(ind):
            rij = np.dot(Q[inde],y)
            R[inde][ind] = rij
            y = y - rij * Q[inde]
        rij = np.linalg.norm(y,2)
        R[ind][ind] = rij
        Q[ind] = y/rij
    # for ind in range(m):
    #     u = transp[ind]
    #     a = transp[ind]
    #     for inde in range(ind):
    #         e = Q[inde]
    #         print()
    #         u = u - (np.dot(a , e) * e)
    #     Q[ind] = u / np.linalg.norm(u,2)
    # for rind in range(m):
    #     row = []
    #     e = Q[rind]
    #     for rinde in range(m):
    #         row.append(np.dot(e, transp[rinde]))
    #     R[rind] = row
    Q = Q.T
    return Q ,R

o = QR_fac(np.array([[1.0,2.0,3.0] , [4.0,5.0,6.0],[7,8,9],[10,11,12]]))

print(o)