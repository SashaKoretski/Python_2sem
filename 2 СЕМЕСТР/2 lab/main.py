import math


def func(x):
    return x ** 2 - 2 * x - 3


def dfunc(x):
    return 2 * x - 2


def newton(a, b, h, eps, Nmax):
    roots = []
    x = a
    while x <= b:
        root_found = False
        fx1 = func(x)
        fx2 = func(x + h)
        if fx1 * fx2 <= 0:
            a1 = x
            a2 = x + h
        n = 1
        while n <= Nmax:
            try:
                xn = a1 - (func(a1) / dfunc(a1))
            except:
                break
            if abs(xn - a1) <= eps:
                roots.append(xn)
                root_found = True
                break
            a1 = xn
            n += 1
            if not root_found:
                print("No convergence after", Nmax, "iterations")
            x += h
    return roots

a = -10
b = 10
h = 0.1
eps = 0.0001
Nmax = 1000

print(newton(a, b, h, eps, Nmax))
