import math


def f1(x):
    return 3*(x**3) + x**2 - x - 5
def f2(x):
    return math.cos(x)**2 + 6 - x

def f(fun , x):
    return fun(x)
def secant(fun,x0,x1):
    tol = 10*(-6)
    xi = x1 - (fun(x1)*(x1 - x0) / (fun(x1) - fun(x0)))
    x0 = x1
    x1 = xi
    while(fun(x1) < tol):
        xi = x1 - (fun(x1)*(x1 - x0) / (fun(x1) - fun(x0)))
        x0 = x1
        x1 = xi
    return xi
