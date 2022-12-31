import numpy as np

# in each row of matrix as data i store persons - age, sigarette packs per year, how long havet hey been a consistant smoker in years
A = [[60,600,3],[40,500,10],[65,1,1],[90,300,76],[16,0,0],[18,100,1] , [18,50,2] , [40,120,20],[70,120,50] , [60,20,2],[25,200,6],[25,30,3]]

# is this vector i store % of lung cancer patients for each people-group corresponding to peoplemat
# this is not an actual data, for that i had to make a request to world health organization and i rather not do that
b = [5,10,0.06,35,0.0001,0.05,0.07,5,30,0.03,0.1,0.02]
# you can add any amount of data and it would still work but A[ind] and b[ind] must be corresponding to eachother


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

# # gram_schmidt qr factorization and calculating x_gram with it
# q_sch,r_sch = QR_fac(peoplemat)
# x_gram = np.linalg.inv(r_sch) @ q_sch.T @ b_chance 

# # housholder method, ficing dimensions of matrixes and calculating x_h with it
# q_h,r_h = QR_haus(peoplemat)
# q_h = q_h.T
# q_h = q_h[0: len(r_h[0])]
# r_h = r_h[0:len(r_h[0]) ]
# q_h = q_h.T
# x_h = np.dot(np.dot(np.linalg.inv(r_h) , q_h.T) , b_chance)

a1 = float(input('input your age: '))
a2 = float(input("how many packs you smoke per year: "))
a3 = float(input('years of consistant smokingew: '))
sw = input('00- type 1 if you want to use gram-schmidt, any other for householder : ')
# creating matrix c and vector d for constrain
c = [[100,700,82] , [18,0,0]]
d = [50.0,0.0001]
AC = A.copy()


# ALGORITHM FOR CALCULATING x_hat FOR CONSTRAINED least squares with qr factorization/gram-schmidt
# these are straight up formulas from readers and books so if it is confusing i can provide material.
if(sw =='1'):
 for el in c:
    AC.append(el)
 Q12,R = QR_fac(AC)
 Q1 = Q12[0:len(A)]
 Q2 = Q12[len(A):]
 Q_hat , R_hat = QR_fac(Q2.T)
 u = np.linalg.solve(R_hat.T, d)
 c = Q_hat.T @ Q1.T @ b - u
 w = np.linalg.solve(R_hat,c)
 y = Q1.T @ b - Q2.T @ w
 x_hat = np.linalg.solve(R,y)

# ALGORITHM FOR CALCULATING x_hat FOR CONSTRAINED least squares with qr factorization/householder
else:
 for el in c:
    AC.append(el)
 Q12,R = QR_haus(AC)
# redimensioning
 R = R[0:len(R[0])]
 Q12 = Q12.T
 Q12 = Q12[:len(R[0])]
 Q12 = Q12.T

 Q1 = Q12[0:len(A)]
 Q2 = Q12[len(A):]
 Q_hat , R_hat = QR_haus(Q2.T)

#  redimensioning
 R_hat = R_hat[0:len(R_hat[0])]
 Q_hat = Q_hat.T
 Q_hat = Q_hat[:len(R_hat[0])]
 Q_hat = Q_hat.T

 u = np.linalg.solve(R_hat.T, d)
 c = Q_hat.T @ Q1.T @ b - u
 w = np.linalg.solve(R_hat,c)
 y = Q1.T @ b - Q2.T @ w
 x_hat = np.linalg.solve(R,y)

# change between x_h and x_gram here for different methods
chance = (np.array([a1,a2,a3]) @ x_hat)
if(chance < 0):
    print('chances are almost 0')
else: print(chance)