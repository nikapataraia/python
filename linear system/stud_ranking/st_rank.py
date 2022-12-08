from audioop import avg
from math import inf, sqrt
import random
import numpy as np

def generate_5x():
    rez = []
    for ind in range(5):
     rez.append(random.randint(50,100))
    return rez

def generate_4x5():
    rez = []
    for ind in range(4):
        rez.append(generate_5x())
    return rez

def frobe(matrix):
    res = 0
    for el in matrix:
        for elem in el:
            res = res + elem**2
    return sqrt(res)

def findavg(mat):
    avg = []
    for el in mat:
        tem = 0
        for ele in el:
            tem = ele + tem
        tem = tem/5
        avg.append(tem)
    return round(sum(avg)/4 , 6)

def infnorm(matrix):
    max = -inf
    for ind in range(len(matrix)):
        res = 0
        for el in matrix:
            res = res + el[ind]
        if(res > max):
            max = res
    return max

def onenorm(matrix):
    max = -inf
    for el in matrix:
        Sum = sum(el)
        if(Sum > max):
            max = Sum
    return max

#TO CHANGE RANDOMLY GENERATED DATA CALL THIS FUNCTION AFTER FORLOOP ON 53
def change_to_provided_data(data):
    global matrixlst_with_id
    temp = []
    for ind in range(len(data)):
        temp.append((ind + 1, data[ind]))
    matrixlst_with_id = temp

matrixlst_with_id = []
for ind in range(1,101):
    matrixlst_with_id.append(( ind, generate_4x5()))


#Frobenius norm
frobdata = []
#first norm
firdata = []
#second norm
secdata = []
#infinite norm
infdata = []
# using avgscores
avgdata = []

for el in matrixlst_with_id:
    frobdata.append((el[0] , round( frobe(el[1]) , 6)))
    firdata.append((el[0] , round( onenorm(el[1]) , 6 ) ))
    secdata.append((el[0] ,round(np.linalg.cond(el[1],2) , 6)))
    infdata.append((el[0] , round(infnorm(el[1]) , 6)))
    avgdata.append((el[0], round(findavg(el[1]) , 6)))


# RANKING 
frobdata = sorted(frobdata,key = lambda x : x[1])
firdata = sorted(firdata,key = lambda x : x[1])
secdata = sorted(secdata,key = lambda x : x[1])
infdata = sorted(infdata,key = lambda x : x[1])
avgdata = sorted(avgdata,key = lambda x : x[1])

print('from bottom to top')
print('fro  one  two  inf  avg')
for ind in range(len(frobdata)):
    print( str(frobdata[ind][0]) + '   ' +str(firdata[ind][0]) + '   ' +str(secdata[ind][0]) + '   ' +str(infdata[ind][0]) + '   ' +str(avgdata[ind][0]))

# using one and infinite norm of a matrix for ranking students would just be stupid so competiotion is between second norm also known as spectral and frobenius norm
# and we see that using matrix frobenius norm and calculating by yearly avg score gives very similar ranking of students




