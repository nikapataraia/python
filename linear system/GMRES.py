from math import inf
import numpy as np


def GMRes(A, b, x0, nmax_iter):
    r = b - np.asarray(np.dot(A, x0)).reshape(-1)

    x = []
    q = [0] * (nmax_iter)
    x.append(x0)
    x.append(r)
    q[0] = r / np.linalg.norm(r)


    h = np.zeros((nmax_iter + 1, nmax_iter))

    for k in range(nmax_iter):
        y = np.asarray(np.dot(A, q[k])).reshape(-1)

        for j in range(k):

            h[j, k] = np.dot(q[j], y)

            y = y - h[j, k] * q[j]

        h[k + 1, k] = np.linalg.norm(y)

        if (h[k + 1, k] != 0 and k != nmax_iter - 1):
            q[k + 1] = y / h[k + 1, k]

        b = np.zeros(nmax_iter + 1)

        b[0] = np.linalg.norm(r)


        result = np.linalg.lstsq(h, b)[0]


        x.append(np.dot(np.asarray(q).transpose(), result) + x0)
    return x

print(GMRes([[1,1,0] , [0,1,0] , [1,1,1]] , [1,0,0] , [0,0,0] , 10))