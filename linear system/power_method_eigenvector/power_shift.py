import numpy as np 

def shifted_power_method(A, sigma, niterations_max=50, tol=1e-15):
    Ashift = A - sigma * np.eye(len(A))
    xn = np.zeros((len(A), niterations_max+1))
    xn[:, 0] = np.ones((len(A),)) + 1e-7*np.random.rand(len(A))
    rn = np.ones((niterations_max+1,))
    for k in range(niterations_max):
        xn[:,k] = xn[:,k] / np.linalg.norm(xn[:,k])
        xn[:,k+1] = np.linalg.solve(Ashift, xn[:,k])
        rn[k+1] = np.sum(xn[:,k+1])/np.sum(xn[:,k])
        if (abs(rn[k+1]-rn[k]) < tol):
            break
    if k < niterations_max:
        rn[k+2:] = rn[k+1] # This ensures the later values are set to something sensible.
    return (1.0/rn[k+1] + sigma, 1.0/rn + sigma, xn[:,k+1]/ np.linalg.norm(xn[:,k+1]))