import numpy as np
import cv2 as cv
import os

curdir = os.path.dirname(os.path.realpath(__file__))
stru = '\yy'
curdir = curdir.replace(stru[0],'/') + '/'

# IMAGE NAME(input)
imagename = ''
# VIDEO NAME(input)
videoname = 'triangle.mp4'
forimage = cv.imread(curdir + imagename)
forvideo = cv.VideoCapture(curdir + videoname)
water = [232,253,255]
coffe = [30,10,10]
greentea = [10,100,10]
def getcolorformula(rgb):
    one = int(np.linalg.norm(np.array(rgb) - np.array(water) , 2))
    two = int(np.linalg.norm(np.array(rgb) - np.array(coffe) , 2))
    three = int(np.linalg.norm(np.array(rgb) - np.array(greentea) , 2))
    allt = one + two + three
    return 'water - ' + str(round(one * 100/allt , 1)) + '%, coffe - ' + str(round(two*100/allt ,  1)) + '%, greentea - ' + str(round(three*100/allt , 1)) +'%'


def issimmilar(vec1,vec2):
    return np.linalg.norm(np.array(vec1) - np.array(vec2) , 1) < 30

def findcontainer(frame):
    frame2 = frame.tolist()
    containercords_frombottomtotop = []
    height = len(frame)
    width = len(frame[0])
    for THid in range(height):
        Hid = height - THid - 1
        left = 0
        right = 0
        disturbed = False
        for Wid in range(width-1):
            if(not issimmilar(frame2[Hid][Wid], frame2[Hid][Wid+1])):
                left = Wid+1
                disturbed = True
                break
        for TWid in range(width-1):
            Wid = width - TWid - 1
            if(not issimmilar(frame2[Hid][Wid], frame2[Hid][Wid-1])):
                right = Wid-1
                break
        for ind in range(left,width-1):
            if(issimmilar(frame2[Hid][ind], frame2[Hid][ind+1])):
                left = Wid+1
                if(left >= right):
                    disturbed = False
            else :
                break
        for ind in range(width - right,width - 1):
            tind = width - ind
            if(issimmilar(frame2[Hid][tind],frame2[Hid][tind-1])):
                right = right - 1
                if(right <= left):
                    disturbed = False
            else :
                break
        # --------------------- marcxena mxare gavakete, exla marjvena darcha
        if(disturbed):
            containercords_frombottomtotop.append((Hid,(left,right)))
    return containercords_frombottomtotop
    # justind = 0
    # print(containercords_frombottomtotop)
    # for el in containercords_frombottomtotop:
    #     hei = el[0]
    #     left = 0
    #     right = 0
    #     for ind in range(el[1][0] , el[1][1] +1):
    #         if(not issimmilar(frame2[hei][ind] , frame2[hei][ind+1])):
    #             left = ind
    #             break  
    #     po = 0 
    #     for ind in range(el[1][0] + 1 , el[1][1] + 1):
    #         ind = el[1][1] - po
    #         if(not issimmilar(frame2[hei][ind] , frame2[hei][ind+1])):
    #             right = ind
    #             break
    #         po = po + 1
    #     containercords_frombottomtotop[justind] = (hei,(left,right))
    #     justind = justind + 1
    # print(containercords_frombottomtotop)

def determinepres(frame,container,containersize):
    x = int((container[len(container) - 1][1][0] + container[len(container) - 1][1][1])/2)
    stopind = 0
    counttop = 0
    # ON THE TRIANGLE TESTCASE BORDER CHANGES IN SIZE
    for ind in range(len(container)):
        # THESE TWO VERY ILLOGICAL IFS ARE HERE ONLY BECAUSE IN GIVEN TEST THE TRIANGLE CHANGES ITS DIMENSIONS (IT WIDENS) and my solution depends on predefined objects shape
        # but if there was no ifs and the object didnt change dimensions range(5,len) would be requered// 
        rind = ind
        if(ind < 20):
            rind = 20
        y = container[rind][0]
        counttop = counttop + container[ind][1][1] - container[ind][1][0]
        if(not issimmilar(frame[y][x],frame[y+1][x])):
            return (((containersize - counttop)/containersize)*100 ,frame[y+1][x])
            # also grabbing frame[y+1][x] to test for liquid consentration


n = 1
istrue,frame = forvideo.read()
print('at frame' , n)
container = findcontainer(frame)
container = list(sorted(container,key=lambda x : x[0]))
contanersize = 0
for el in container:
    contanersize = contanersize + el[1][1] - el[1][0]
pros = determinepres(frame,container,contanersize)
print(pros[0],'%')
print(getcolorformula(pros[1]))
cv.imshow('press d to exit',frame)
n = 2
while True:
    # TRY-CATCH BECAUSE OF VIDEOPLAYER ERROR, exmaple had 100frames but after 100th frame while loops does not stop(we dont know cv library good enough so i wont even try to correct it)
    try:
     istrue,frame = forvideo.read()
     print('at frame' , n)
     pros = determinepres(frame,container,contanersize)
     print(pros[0],'%')
     print(getcolorformula(pros[1]))
     n+=1
     cv.imshow('press d to exit',frame)
     if cv.waitKey(20) & 0xFF == ord('d'):
        break
    except:
        break
forvideo.release()
cv.destroyAllWindows()

# first thing i do is i take first frame of the video and search for the instrument that we will be filling with our liquid
# i call it container, and it is array of tuples which store one y cord and tuple of x cords
# so basically container stores every y on which our contaner is located with two x coordinats
# after that i take this contaner and for every frame i go down from highest y to lowest add up all of x2 - x1 cords which gives us volume of the not yet filled vessel 
# and if i find distortion in color in my way i stop and calculate (entire vol) - (added up vol) to calculate filled up space
# (i forgot to say when im calculating container cords i try to eliminate all of the borders from the actual cords where the luqid can go, but i think i failed miserably 
# and dont know why, thats why in determinepres function, in for loop u see if(ind < 20) cuz i have to jump over some pixels so it does not detect distortion straight away
# thats why there might be slight miscalculations, so im not happy with this algorithm)