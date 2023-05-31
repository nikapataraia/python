from msilib.schema import Error
import numpy as np

while(True):
    while(True):
     try:
        x = int(input())
        break
     except ValueError:
        print("enter number")
    if(x > 0 and x <= 1000):
        break
myarr = []
myvec = []
for ind in range(x):
    tempar = []
    for ind2 in range(x):
        while(True):
            try:
             y = float(input())
             break
            except ValueError:
             print("enter number")
        tempar.append(y)
    myarr.append(tempar)


for ind in range(x):
    while(True):
            try:
             t = float(input())
             break
            except ValueError:
             print("enter number")
    myvec.append(t)


# mysecarr = myarr
# if(x >= 11):
#     mysecarr[10][10] = mysecarr[10][10] + 0.0001
# else :
#     mysecarr[0][0] = mysecarr[0][0] + 0.0001
def changejustalittlebit(arr):
    newarr = arr
    if(x >= 11):
        newarr[10][10] = newarr[10][10] + 0.0001
    else :
        newarr[0][0] = newarr[0][0] + 0.0001
    return newarr



def systemsolve(A,b):
    mat = np.matrix(A)
    b = np.array(b)
    return np.linalg.inv(A).dot(b)

before = systemsolve(myarr,myvec)
after = systemsolve(changejustalittlebit(myarr), myvec)
print(before)
print("after change -")
print(after)

def determinecondition(a,b):
    a = np.array(a)
    b = np.array(b)
    rt = np.linalg.norm(a,2)/np.linalg.norm(b,2)
    if(rt > 1):
        return 0
    return 1

if(determinecondition(after,before) == 0):
    print("the system is well-conditioned")
else :
    print('The system is ill-conditioned')
