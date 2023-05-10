import numpy as np
import cv2 as cv
import os
curdir = os.path.dirname(os.path.realpath(__file__))
stru = '\yy'
curdir = curdir.replace(stru[0], '/') + '/'
im_name = 'Capture1.PNG'
blur_arr1 = np.array([[0.003,0.013,0.022,0.013,0.003] , 
                      [0.013,0.05,0.078,0.05,0.098], 
                      [0.022, 0.078, 0.114, 0.078, 0.022], 
                      [0.013, 0.05, 0.078, 0.05, 0.098],
                      [0.003, 0.013, 0.022, 0.013, 0.003]
                      ])

blur_arr3 = np.array([
    [0.003,0.013,0.022,0.013,0.003],
    [0.013,0.06,0.098,0.06,0.013],
    [0.022, 0.098, 0.162, 0.098, 0.022],
    [0.013, 0.06, 0.098, 0.06, 0.013],
    [0.003, 0.013, 0.022, 0.013, 0.003]
])
num3x3 = 1/9
blur_arr2 = np.array([[num3x3,num3x3,num3x3],
                      [num3x3, num3x3, num3x3],
                      [num3x3, num3x3, num3x3]])

blur_arr4 = np.array([[1/16,1/8,1/16],
                      [1/8,1/4,1/8],
                      [1/16,1/8,1/16]])

conv_arr2 = np.array([[-0.25, -0.5, -0.25], 
                      [0, 0, 0], 
                      [0.25, 0.5, 0.25]])

conv_arr1 = np.array([[0.125, 0.125, 0.3, 0.125, 0.125],
                     [0, 0, 0, 0, 0], 
                     [-0.125, -0.125, -0.3, -0.125, -0.125]])

def grayscale(img):
    return cv.cvtColor(img,cv.COLOR_BGR2GRAY)

def conv_img_mat(img,conv_mat):
    result = []
    step_size = int(len(conv_mat)/2)
    for i in range(len(img)):
        row = []
        for j in range(len(img[0])):
            vec = np.zeros(3)
            for i_2 in range(len(conv_mat)):
                for j_2 in range(len(conv_mat)):
                    try:
                        vec = vec + conv_mat[i_2][j_2] * img[i -step_size + i_2][j - step_size + j_2]
                    except:
                        pass
            vec = list(map(lambda x: int(x), vec))
            row.append(vec)
        result.append(row)
    return result

def cleare_edged(img,le):
    for i in range(len(img)):
        for j in range(len(img[0])):
            vec = np.zeros(3)
            for i_2 in range(le):
                for j_2 in range(le):
                    try:
                        vec = vec + img[i - int(le/2) + i_2][j - int(le/2) + j_2]
                    except:
                        pass
            vec = list(map(lambda x: int(x/(le**2)), vec))
            if(np.linalg.norm(vec) < 240):
                img[i][j] = [255,255,255]
            else :
                img[i][j] = [0,0,0]



def edged_img(img, edge_arr, blur_arr, with_grayscale=True ,with_blend=True):
    if(with_grayscale):
        img = grayscale(img)
    if(with_blend):
        img = conv_img_mat(img,blur_arr)
        img = np.array(img).astype(np.uint8)
    on_y = conv_img_mat(img, edge_arr)
    on_x = conv_img_mat(img,edge_arr.T)
    result = np.sqrt(np.square(on_y) + np.square(on_x))
    result *= 255.0 / result.max()
    # cleare_edged(result,3)
    return result


def houghtransf(pic):
    height, width = len(pic),len(pic[0])
    Amc = np.zeros((int(height/5), int(width/5)))
    for i in range(0,height-0):
        for j in range(0,width-0):
            if (np.linalg.norm(pic[i][j] > 150)):
                # j = m*i + c
                # c = -m*i + j
                for m in range(int(width/5)):
                    c = -m*i + j
                    if (c >= 0 and c < int(height/5)):
                        Amc[c][m] = Amc[c][m] + 1
    
    first_max = np.where(Amc == np.amax(Amc))
    print(first_max)
    print(Amc[1][0])


path = curdir + im_name
newd = cv.imread(path)
newd = edged_img(newd,conv_arr2,blur_arr4,True,True)
newd = np.array(newd)
newd = newd.astype(np.uint8)

houghtransf(newd)
cv.imshow('edged',newd)
cv.waitKey(0)

