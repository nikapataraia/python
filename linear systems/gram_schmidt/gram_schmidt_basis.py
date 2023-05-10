import numpy as np
def gram_schmid_basis(v):
    def proj(ve1, ve2):
        return ve1 * (np.dot(ve2, ve1) / np.dot(ve1, ve1))
    u = []
    for i in range(len(v)):
        tmp = v[i]
        lnu = len(u)
        for ind in range(lnu):
            tmp = tmp - proj(u[ind] , v[lnu])
            if(not (np.array(tmp)).any()):
                return None

        u.append(np.array(tmp))
    u = list(map(lambda x : x/np.linalg.norm(x,len(u[0])) , u))
    return u