import numpy as np

def crout_LU(A):
    for ind in range(len(A)):
        el = list(map(lambda x : float(x),A[ind]))
        A[ind] = el
    A = np.array(A)
    n = A.shape[0]
    
    U = np.zeros((n, n), dtype=np.double)
    L = np.zeros((n, n), dtype=np.double)
    
    for k in range(n):
        
        L[k, k] = A[k, k] - L[k, :] @ U[:, k]
        
        U[k, k:] = (A[k, k:] - L[k, :k] @ U[:k, k:]) / L[k, k]
        L[(k+1):, k] = (A[(k+1):, k] - L[(k+1):, :] @ U[:, k]) / U[k, k]
    
    return L, U


print(crout_LU([[2,4,2],[1,1,2],[-1,0,2]]))