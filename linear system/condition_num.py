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
for ind in range(x):
    tempar = []
    for ind2 in range(x):
        while(True):
            try:
             y = int(input())
             break
            except ValueError:
             print("enter number")
        tempar.append(y)
    myarr.append(tempar)



def conditionofmatrix(arr):
    matrix = np.matrix(arr)
    return np.linalg.cond(matrix)




