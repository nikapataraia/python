from math import inf
import math
import os
import random
import numpy as np
import cv2 as cv


curdir = os.path.dirname(os.path.realpath(__file__))
stru = '\yy'
curdir = curdir.replace(stru[0],'/') + '/'
encodingks = []
imgwidth =0
imgheight = 0
stringlength = 0
floatmul = 1

def custom_dot_mat(a , b):
    res = []
    for ind in range(len(a)):
        row = []
        for inde in range(len(b[0])):
            row.append(0)
        res.append(row)
    for ind in range(len(a)):
        for inde in range(len(b[0])):
            for elind in range(len(b)):
                res[ind][inde] += a[ind][elind] * b[elind][inde]
    return res

def custom_dot_vec(a,b):
    res = []
    for ind in range(len(a)):
        res.append(0)
    for ind in range(len(a)):
        for inde in range(len(a[ind])):
            res[ind] += a[ind][inde] * b[inde]
    return res

 
def largest(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def turn_float(y):
    global floatmul
    max = largest(y)
    while(max < 262144):
        floatmul = floatmul * 10
        max = max*10
    return np.array(list(map(lambda x : x * floatmul , y)))


#  ITERATIVE METHODS
def SOR(n,matr,bientries,xientries,tolerance,maximumit,wO):
    if(tolerance < 0):
        tolerance = - tolerance
    def ite(v,w):
        elements = []
        for el in v:
            elements.append(el)
        def calcinw(ind):
            result = bientries[ind]
            for indx in range(n):
                if(indx!=ind):
                    result = result - matr[ind][indx] * elements[indx]
            return result/matr[ind][ind]

        for ind in range(n):
            elements[ind] = elements[ind] * (1-w) + w * calcinw(ind)
        return elements

    def tol(pre,new):
        mat = np.array(pre) - np.array(new)
        return np.linalg.norm(mat,inf) <= tolerance

    prev = xientries
    res = []
    for rn in range(maximumit):
        res = ite(prev,wO)
        if(tol(prev,res)):
            return (list(map(lambda x : round(x) , res)) ,rn)
        prev = res
    return None

def jacobi(n,mat,b,x,tol,maxIT):
    def tole(pre,new):
        vec = np.array(pre) - np.array(new)
        return np.linalg.norm(vec,inf) <= tol
    def ite(pr):
        prev = []
        elements = []
        for el in pr:
            prev.append(el)
            elements.append(el)
        def calc(ind):
            res = b[ind]
            for indx in range(n):
                if(ind != indx):
                    res = res - mat[ind][indx] * prev[indx]
            return res/mat[ind][ind]
        for ind in range(n):
            elements[ind] = calc(ind)
        return elements
    prev = []
    for el in x:
        prev.append(el)
    res = []
    for t in range(maxIT):
        res = ite(prev)
        if(tole(prev,res)):
            return (list(map(lambda x : round(x) , res)),t)
        prev = res
    return None

         
def gausseidl(n,mat,b,x,tol,maxIT):
    def ite(v):
        elements = []
        for el in v:
            elements.append(el)
        def calcinw(ind):
            result = b[ind]
            for indx in range(n):
                if(indx!=ind):
                    result = result - mat[ind][indx] * elements[indx]
            return result/mat[ind][ind]

        for ind in range(n):
            elements[ind] = calcinw(ind)
        return elements

    def tole(pre,new):
        mat = np.array(pre) - np.array(new)
        return np.linalg.norm(mat,inf) <= tol

    prev = x
    res = []
    for rn in range(maxIT):
        res = ite(prev)
        if(tole(prev,res)):
            return (list(map(lambda x : round(x) , res)),rn)
        prev = res
    return None

def richardson(n , a ,b , x,tol,maxIT,p,t):
    prev = x
    new = x
    p_inv = np.linalg.inv(p)
    # dot_pin_a = np.dot(np.array(p_inv), np.array(a))
    dot_pin_a = custom_dot_mat(p_inv , a)
    dot_ping_b = np.array(custom_dot_vec(p_inv , b) )* t
    # dot_ping_b = np.dot(np.array(p_inv) , b)  * t
    i  = np.identity(n)
    def tole(pre , ne):
        mat = np.array(pre) - np.array(ne)
        return np.linalg.norm(mat,inf) <= tol
    def ite(v):
        matp = i - t * dot_pin_a
        return np.dot(matp , v) + dot_ping_b
    for rn in range(maxIT):
        new = ite(prev)
        if(tole(new,prev)):
            print(new)
            return (list(map(lambda x : round(x) , new)),rn)
        prev = new
    return None

# ________________________________________________________________________________________________________________________________________
    
# creating K
def create_k(n):
    res = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if( i == j):
                tmp.append((3 * n))
            else :
                tmp.append(random.randint(0,5))
        res.append(tmp)
    return np.array(res)


# _________________________________________________________________________________________________________________________________________

# Gram-Schmid

def gram_schmid_basis(v):
    
    def proj(ve1, ve2):
        return ve1 * (np.dot(ve2, ve1) / np.dot(ve1, ve1))
    u = []
    for i in range(len(v)):
        tmp = v[i]
        lnu = len(u)
        for ind in range(lnu):
            tmp = tmp - proj(u[ind] , v[lnu])
            if(not (np.array(tmp)).any()):
                return None

        u.append(np.array(tmp))
    u = list(map(lambda x : x/np.linalg.norm(x,len(u[0])) , u))
    return u

def check_invertibility(set):
    vecspace = gram_schmid_basis(set)
    if(vecspace is None):
        return False
    return True


# ---------------------------------


def str_to_ord(strin):
    orded = []
    for el in strin:
        orded.append(ord(el))
    return orded

def get_y(k,orde):
    return np.dot(k,orde)

def encode_sequence(seq , n):
    global stringlength
    stringlength = len(seq)
    k = create_k(n)
    while(not check_invertibility(k)):
        k = create_k(n)
    encodingks.append(k)
    result = []
    arr = seq.copy()
    while(len(arr) > 0):
        m = len(arr)
        if(m == 0):
            break
        if(m < n):
            newk = create_k(m)
            while(not check_invertibility(newk)):
                newk = create_k(m)
            encodingks.append(newk)
            for el in get_y(newk,arr):
                result.append(round(el))
            break
        else :
            for el in get_y(k,arr[0:n]):
                result.append(round(el))
        arr = arr[n:]
    return result

def encfor_mat(mat, n): 
    global imgwidth,imgheight
    imgheight = len(mat)
    imgwidth = len(mat[0])
    x = []
    for el in mat:
        for rgb in el:
            for info in rgb:
                x.append(info)
    return encode_sequence(x,n)

def decode_y(y):
    x = []
    n = len(encodingks[0])
    arr = y.copy()
    n = len(encodingks[0])
    while(len(arr) > 0):
        m = len(arr)
        if(m < n):
            n = len(arr)
            l = gausseidl(n , encodingks[1],arr,[0] * n , 10**(-10) , 1000)
            for el in l[0]:
                x.append(round(el))
            break
        else :
            l = gausseidl(n , encodingks[0] , arr[0:n],[0] * n, 10**(-10),1000)
            for el in l[0]:
                x.append(el)
        arr = arr[n:]
    return x

# def genbigarr():
#     res = []
#     for _ in range(10000):
#         res.append(random.randint(0,256))
#     return res
# a = genbigarr()
# b = encode_sequence(a, 15)
# d = decode_y(b)
# for ind in range(len(a)):
#     if(a[ind] != d[ind]):
#         print('at least one')

def build_img(decoded):
    img_mat = []
    for ind in range(len(decoded) / 3):
        row = []
        for _ in range(imgwidth):
            row.append((decoded[ind] , decoded[ind + 1] , decoded[ind + 2]))
        img_mat.append(row)
    return img_mat


def build(arr ,he ,wi) :
    img = []
    tmp = arr.copy()
    split1 = []
    while(len(tmp) != 0):
        split1.append(tmp[:wi * 3])
        tmp = tmp[wi * 3:]
    for el in split1:
        tmp = el.copy()
        row = []
        while(len(tmp) != 0):
            row.append(tmp[:3])
            tmp = tmp[3:]
        img.append(row)
    return np.array(img)

    
    # for ind in range(he):
    #     row = []
    #     for inde in range(wi):
    #         rgbg = []
    #         for rgb in range(3):
    #             rgbg.append(arr[ind * wi + inde * 3 + rgb])
    #         rgbg = (rgbg[0] ,rgbg[1] ,rgbg[2])
    #         row.append(rgbg)
    #     img.append(np.array(row))
    # return np.array(img)


def flatten(img):
    res = []
    for el in img:
        for ele in el:
            for rgb in ele:
                res.append(rgb)
    return res

def hide_in_plain_sight(img, encoded): 
    encoded_in_bi = list(map(lambda x : bin(x)[2:].zfill(18) , encoded))
    j = 0
    i = 0
    maxj = len(img)
    maxi = len(img[0])
    trojan_img = img.copy()
    for el in encoded_in_bi:
        for ind in range(3):
            substr = ''
            if(ind == 0):
                substr = el[0:6]
            if(ind == 1):
                substr = el[6:12]
            if(ind == 2):
                substr = el[12:18]
            if(i == maxi):
                j = j+1
                i = 0
            if(j == maxj):
                print('given encoded message was too big')
                return None
            imgpix = trojan_img[j][i]
            r = bin(imgpix[0])[2:].zfill(18) 
            g = bin(imgpix[1])[2:].zfill(18)
            b = bin(imgpix[2])[2:].zfill(18)
            r = r[:16] + substr[0:2]
            g = g[:16] + substr[2:4]
            b = b[:16] + substr[4:6]
            trojan_img[j][i] = (int(r , 2), int(g , 2), int(b,2))
            i = i+1
    return trojan_img

def hidden_in_plain_sight_mat(img):
    iteration = imgheight * imgwidth * 3
    j = 0
    i = 0
    maxj = len(img)
    maxi = len(img[0])
    encoded_arr = []
    temp = img.copy()
    for ind in range(iteration):
        stri = ""
        for _ in range(3): 
            if(i == maxi):
                j = j+1
                i = 0
            if(j == maxj):
                print('something went wrong')
                return None
            rgb = temp[j][i]
            for el in rgb:
                stri = stri + bin(el)[2:].zfill(18)[16:]

        # for el in img[j][i]:
        #     str = str + bin(el[0])[2:].zfill(12)[10:]+ bin(el[1])[2:].zfill(12)[10:]+ bin(el[2])[2:].zfill(12)[10:]
            i = i+ 1
        inte = int(stri,2)
        encoded_arr.append(inte)
    return decode_y(encoded_arr) 

def hidden_in_plain_sight_str(img):
    iteration = stringlength
    j = 0
    i = 0
    maxj = len(img)
    maxi = len(img[0])
    encoded_arr = []
    temp = img.copy()
    for ind in range(iteration):
        stri = ""
        for _ in range(3): 
            if(i == maxi):
                j = j+1
                i = 0
            if(j == maxj):
                print('something went wrong')
                return None
            rgb = temp[j][i]
            for el in rgb:
                stri = stri + bin(el)[2:].zfill(18)[16:]

        # for el in img[j][i]:
        #     str = str + bin(el[0])[2:].zfill(12)[10:]+ bin(el[1])[2:].zfill(12)[10:]+ bin(el[2])[2:].zfill(12)[10:]
            i = i+ 1
        inte = int(stri,2)
        encoded_arr.append(inte)
    return decode_y(encoded_arr) 

def create_trojan_horse(img,n):
    encoded_sequence = encfor_mat(img,n)
    horse = cv.imread(curdir + 'north.jpg')
    trojan_horse = hide_in_plain_sight(horse , encoded_sequence)
    return trojan_horse



x = str(input('type 0 if its an image, any other if its a string : '))
if(x == '0'):
    imgpath = input('image path : ')
    matrix = cv.imread(curdir + imgpath)
    horse = create_trojan_horse(matrix,30)
    cv.imwrite( curdir + '1m.png',np.array(horse))
    decoded_img = hidden_in_plain_sight_mat(horse)
    img = build(decoded_img,imgheight,imgwidth)
    # for ind in range(len(img)):
    #     print('------L')
    #     print(img[ind])
    #     print(matrix[ind])
    #     print('------')
    cv.imwrite(curdir + '2m.png',np.array(img))
else :
    stri = input("string : ")
    horse = cv.imread(curdir + 'arthas.jpg')
    encoded = encode_sequence(str_to_ord(stri) , 3)
    trojan_horse = hide_in_plain_sight(horse ,encoded)
    cv.imwrite( curdir + '1s.png',np.array(trojan_horse))
    decoded_int = hidden_in_plain_sight_str(trojan_horse)
    decoded_str = ''
    for el in decoded_int:
        decoded_str = decoded_str + chr(el)

    print('encoded string : ' + decoded_str)



    # --------------------
    # h = len(img)
    # w = len(img[0])
    # encoded_in_bi = list(map(lambda x : bin(x)[2:].zfill(12) , encoded))
    # img_flattened = flatten(img)
    # img_binary_flattened = list(map(lambda x : bin(x)[2:].zfill(12) , img_flattened))
    # for ind in range(len(encoded_in_bi)):
    #     for inde in range(6):
    #         imgpix = img_binary_flattened[ind*6 + inde]
    #         change = encoded_in_bi[ind][inde*2] + encoded_in_bi[ind][inde *2 +1] 
    #         imgpix = imgpix[:2] + change
    #         img_binary_flattened[ind] = imgpix

    # img_flattened = list(map(lambda x : int(x , 2) , img_binary_flattened))
    # result = []
    # for ind in range(h):
    #     row = []
    #     for inde in range(w):
    #         rgb = []
    #         for eli in range(3):
    #             rgb.append(img_flattened[ind*w + inde * 3 + eli])
    #         rgbt = (rgb[0] , rgb[1] , rgb[2])
    #         row.append(rgbt)
    #     result.append(row)
    # return build(img_flattened , h , w)
    # --------------------

    # flattened_img = flatten(img)
    # flattened_img_binary = list(map(lambda x :bin(x)[2:].zfill(8) , flattened_img ))
    # result_flattened_binary = []
    # for j in range(imgheight):
    #     for i in range(imgwidth):
    #         el = ''
    #         for eachnum in range(4):
    #             el = el + flattened_img_binary[j * imgwidth + i * 4 + eachnum]
    #         result_flattened_binary.append(el)
    # result_flattened = list(map(lambda x : int(x,2) , result_flattened_binary))
    # return result_flattened
    # ----------------------------------------------