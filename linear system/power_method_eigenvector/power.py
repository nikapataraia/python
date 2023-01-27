import numpy as np
def find(A,x):
    tol = 10^-6
    max_iter = 100
    lam_prev = 0
    for i in range(max_iter):
        x = A@x/ np.linalg.norm(A@x)
        lam = (x.T @ A @ x) / (x.T @x)
        if(np.abs(lam - lam_prev) < tol):
            return lam
        lam_prev = lam
    print('iterations exceeded')
    return lam,x