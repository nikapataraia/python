import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 3*(x**3) + x**2 - x - 5

def f(x):
    return x**2

def regular_falsi(a, b, tol, maxiter,f):
    for i in range(maxiter):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
        plt.axvline(c, color='r', linestyle='--')
    return c

a = 1
b = 4
tol = 1e-15
maxiter = 20

x = np.linspace(0, 5, 100)
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')

# Run the regular falsi method
root = regular_falsi(a, b, tol, maxiter,f)
print(root)
# Plot the final root and legend
plt.axvline(root, color='g', linestyle='-', label='Root')
plt.legend()
plt.show()
