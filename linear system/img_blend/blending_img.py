import os
import cv2 as cv
import numpy as np

def rescale(frame,scalewidth,scaleheaight):
    return cv.resize(frame, (int(frame.shape[1] * scalewidth), int(frame.shape[0] * scaleheaight)) , interpolation=cv.INTER_AREA)

def imgdim(img):
    return img.shape[1]/img.shape[0]


#if you want to change image size, just change the number 712 to the width that you want it to be in it will do everything else on its own
def blend(path1,path2,ind):
    img1 = cv.imread(path1)
    tempind = imgdim(img1)
    if(tempind >= 1):
        img1 = rescale(img1,  712/img1.shape[1], (712 / tempind)/img1.shape[0])
    else:
        img1 = rescale(img1, (712*tempind)/img1.shape[1], 712/img1.shape[0])
    img2 = cv.imread(path2)
    img2 = rescale(img2, img1.shape[1]/img2.shape[1], img1.shape[0]/img2.shape[0])
    matrix1 = np.array(img1)
    matrix2 = np.array(img2)
    matrix1 = matrix1 * ind
    matrix2 = matrix2 * (1 - ind)
    return (matrix1 + matrix2).astype(np.uint8)
    


curdir = os.path.dirname(os.path.realpath(__file__))
stru = '\yy'
curdir = curdir.replace(stru[0],'/') + '/'


#CHANGE IMAGE NAMES HERE ------------------------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# but directory must be current folder, or imgpath = (img directory)
img1path = curdir +'arthas.jpg'
img2path = curdir + 'north.jpg'
imgarr = []
for ind in range(0,240):
    imgarr.append(blend(img1path,img2path,ind/240))




#saves video in current directory
out = cv.VideoWriter(curdir + 'project.avi',cv.VideoWriter_fourcc(*'DIVX'), 20, (imgarr[0].shape[1],imgarr[0].shape[0]))
for i in range(len(imgarr)):
    out.write(imgarr[i])

out.release()

myvid = cv.VideoCapture(curdir + 'project.avi')
while True:
    isTrue, frame = myvid.read()
    try:
     cv.imshow('press d to exit' , frame)
    except:
        pass
    if(cv.waitKey(20) & 0xFF == ord('d')):
        break
myvid.release()
cv.destroyAllWindows()




