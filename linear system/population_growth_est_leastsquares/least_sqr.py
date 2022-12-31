import numpy as np

start = 1950
years = []
for ind in range(73):
    years.append([ind])

growth = [0.0,1.75,1.85,1.93,1.96,2.01,2.00,2.03,2.04,1.86,1.65,1.63,1.90,2.21,2.24,2.14,2.08,2.03,2.05,2.08,2.06,2.02,1.98,1.96,1.92,1.85,1.80,1.77 , 1.75 , 1.77, 1.80,1.81,1.84,1.82,1.79,1.80,1.82,1.84,1.81,1.78,1.77 , 1.69,1.60,1.54,1.49,1.46,1.43,1.40,1.37,1.34,1.34,1.33,1.31,1.29,1.28,1.27,1.27,1.27,1.27,1.27,1.27,1.25,1.25,1.24,1.22,1.19,1.17,1.15,1.10,1.06,0.98,0.87,0.83]

# this has nothing to do with solution of this project, its a graph function for y = ax + b of the given cords.
def getgraph(y,x):
    length = len(y)
    if(length != len(x)):
        print('data is not consistant')
        return (0,0)
    sigx = 0
    sigy = 0
    sigxy = 0
    sigx2 = 0
    for ind in range(length):
        tx = x[ind]
        ty = y[ind]
        sigx += tx
        sigy += ty
        sigxy += tx * ty
        sigx2 += tx * tx
    a = (length * sigxy - sigy * sigx) / (length * sigx2 - sigx * sigx)

    b = (sigy - a * sigx) / length
    return (a,b)
# estimation for y = ax + b
def estimate(x,equ):
    a = x - 1950
    return equ[0] * a + equ[1]

# modified gram-schmidt
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
    Q = Q.T
    return Q ,R

def haus(v):
    length = len(v)
    return np.identity(length) - (2 * np.outer(v , v.T) / np.dot(v.T,v))

# householder
def QR_haus(A):
    A = np.array(A)
    m = len(A)
    n = len(A[0])
    Q = np.identity(m)
    R = A.copy()
    for ind in range(n):
        transpose = R.T
        ln = m - ind
        e = np.zeros(ln)
        e[0] = 1
        v = np.array(transpose[ind][ind:])
        s = 1
        if(v[0] < 0):
            s= -1
        v = v + s* np.linalg.norm(v,2) * e.T
        H = haus(v)
        filled_h = np.identity(m)
        for filind in range(len(H)):
            for filinde in range(len(H)):
                filled_h[filind + ind][filinde + ind] = H[filind][filinde]
        R = filled_h @ R
        Q = Q @ filled_h
    return Q,R


# finding q,r of both methods
q,r = QR_fac(years[50:])
q_h , r_h = QR_haus(years[50:])
b = growth[50:]

# gram-qr finding x
x = np.dot(np.dot(np.linalg.inv(r) , q.T) , b)

# fixing dimension problem in housholder q,r
q_h = q_h.T
q_h = q_h[0: len(r_h[0])]
r_h = r_h[0:len(r_h[0]) ]
q_h = q_h.T
x_h = np.dot(np.dot(np.linalg.inv(r_h) , q_h.T) , b)

# making prediction by using given x
def estimate_qr(num):
    num = num - 2000
    # change through x_h and x if you want to switch up between householder and gram-qr
    return [[num]] @ x_h 


a = input('input year on which you wish to make an estimation : ')
print(estimate_qr(int(a)))