import numpy as np

def crout_LU(A):
    for ind in range(len(A)):
     el = list(map(lambda x : float(x),A[ind]))
     A[ind] = el
    A = np.array(A)

    n = A.shape[0]
    

    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)
    

    for i in range(n):
        for k in range(i, n): 
            if ~np.isclose(U[i, i], 0.0):
                break
            U[[k, k+1]] = U[[k+1, k]]
            P[[k, k+1]] = P[[k+1, k]]
            

        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]


        
    return P, L, U