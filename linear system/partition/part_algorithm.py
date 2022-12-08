import numpy as np
import math
import random

#TO CHANGE RANDOMLY GENERATED DATA CALL THIS FUNCTION AFTER first FORLOOP ON 21 BUT BEFORE SORTING ON STUDEMATRIX_NORM_2
def change_to_provided_data(data):
    global students,studematrix_norm_2
    temp1 = []
    temp2 = []
    for ind in range(len(data)):
        temp1.append((ind+1 , data[ind]))
        temp2.append((ind+1, round(np.linalg.norm(data[ind],2), 2 )))
    students = temp1
    studematrix_norm_2 = temp2

students = []
studematrix_norm_2 = []

# apeending in studematrix_norm_2 student id with second norm of their score vectors
for ind in range(1,251):
    temp = []
    for ln in range(0,3):
        temp.append(random.randint(50,100))
    students.append((ind , temp))
    studematrix_norm_2.append((ind,round(np.linalg.norm(temp,2), 2 )))


# change_to_provided_data(SOME DATA(array of 3x vectors)   )


# sorting both lists by student scores
studematrix_norm_2 = sorted(studematrix_norm_2,key = lambda x : x[1])


# GROUPING BY COMPARING EUCLEDIAN(second) NORM OF SCORE VECTORS
# we could also use first norm which would just be a sum of all 3 scores but theres a difference in these two
# second norm values student who has high score in one of the subjects but low in another
# for exmp stud1 (a,b) and stud2 (c,d) a + b = c + d but consider that highest num is a
# secnorm(stud1) > secnorm(stud2) but firstnorms are equal
# i just chose to give higher priority to (a,b) students
# and it represents the distance between this point and the origin so its more logical
grouped_2norm = [[] , [] , [] , [] , [] ,[] , [] , [] , [] , [] ,[] , [] , [] , [] , [] ]
i = True
for ind in range(15):
    for ind2 in range(15):
        if(i):
            grouped_2norm[ind2].append(studematrix_norm_2[ind * 15 + ind2])
        else :
            grouped_2norm[ind2].append(studematrix_norm_2[ 225 - ind * 15 - ind2])
    i = not i

def func(x):
    rez = []
    for el in x:
        rez.append(el[0])
    return rez

only_ids_2 = list(map(func,grouped_2norm))
print(only_ids_2)
grouped_vectorscores = []


# NOW JUST CREATING MATRIXES FOR GROUPED STUDENTS, 
for el in only_ids_2:
    temp = []
    for elem in el:
        # this is because the students array is already sorted
        temp.append(students[elem - 1][1])  
    grouped_vectorscores.append(temp)


for el in grouped_vectorscores:
    print('--------')
    print(np.matrix(el))
    print(np.linalg.norm(el,'fro'))
    print('--------')



# would not store these many arrays for one execution but every step of the puzzle in encoded in them

# only_ids_2 - grouped students, IDs
# grouped_vectorscores - grouped students, score vectors
# grouped_2norm - grouped students by the second norm of a vector
# students - array of student IDs and their vectors
# studematrix_norm_2 - array of student IDs and their vectors second norms
