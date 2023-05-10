import math


def f1(x):
    return 3*(x**3) + x**2 - x - 5
def f2(x):
    return math.cos(x)**2 + 6 - x

def f(fun , x):
    return fun(x)


def bisection(fu,starting_inv = -10**(10)):
    a = starting_inv
    b = a
    k = f(fu,b)
    tol = 10**(-15)
    if(abs(k) < tol):
       return b
    leftsided = k < 0
    if(leftsided):
        while(k < 0):
            b = b + 100
            k = f(fu,b)
            if(k > 0):
                interval = (a,b)
            a = b 
    else:
        while(k > 0):
            b = b + 100
            k = f(fu,b)
            if(k < 0):
                interval = (a,b)
            a = b 
    mid = (interval[0]+interval[1])/2
    while(abs(k) >= tol):
        mid = (interval[0]+interval[1])/2
        k = f(fu,mid)
        if(leftsided and (k < 0)):
            interval = (mid,interval[1])
        if(leftsided and (k > 0)):
            interval = (interval[0],mid)
        if((not leftsided) and (k < 0)):
            interval = (interval[0],mid)
        if((not leftsided) and (k > 0)):
            interval = (mid,interval[1])
    return round(mid,6)

print(bisection(f1))
print(bisection(f2))