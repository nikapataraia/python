import numpy as np

def svd(A):
    A= np.array(A)
    forsing = A.T@A
    ev,V = np.linalg.eigh(forsing)
    U = []
    for ind in range(len(V)):
        u = A@V[:,ind]/np.linalg.norm(A@V[:,ind])
        U.append(u)
    U = np.array(U)
    U = U.T
    D = U.T @ A @ V
    return np.array(U),np.array(D),np.array(V.T)


u,d,v = svd([[1,2,3],[4,5,6],[7,8,10]])
# NOTICE!! if det(A) = 0, this wont give exact values of A but an a aproximation of it
print(u@d@v)
