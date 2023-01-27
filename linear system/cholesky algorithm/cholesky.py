import numpy as np
from math import sqrt
def cholesky(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]

    for i in range(n):
        for k in range(i + 1):
            tmp = sum(L[i][j] * L[k][j] for j in range(k))
            if(i == k):
                
                L[i][k] = sqrt(A[i][i] - tmp)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp))
    return np.array(L)

L = cholesky([[2,-3],[-3,3.1]])
print(L @L.T)

# NOTICE, A must be positive definite and symetric matrix matrix