# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:25:05 2021

@author: antony
"""

from math import sin
from math import cos
from math import tan
from math import exp
from math import log
from math import acos
from math import atan
from math import asin
from math import sqrt


def Newton(f, fder, x0, epsilon, Nitermax):
    n=0
    xold = x0
    erreur = -(f(xold)/(fder(xold)))

    while abs(erreur) > epsilon and n < Nitermax :
        xnew = xold - f(xold)/fder(xold)
        n += 1
        erreur = xnew - xold
        xold = xnew
        print(n,xnew)
    return xnew



def f1(x):
    return (x**4) + 3*x -9

def fder1(x):
    return 4 * (x**3) + 3


def f2(x):
    return x - 3 * cos(x) + 2

def fder2(x):
    return 1 + 3*sin(x)


def f3(x):
    return x*exp(x)-7

def fder3(x):
    return exp(x) + x*exp(x)


def f4(x):
    return exp(x) - x - 10

def fder4(x):
    return -1 + exp(x)
    

def f5(x):
    return 2*tan(x) - x - 5

def fder5(x):
    return 1 + 2*tan(x)**2
    

def f6(x):
    return exp(x) - (x**2) - 3

def fder6(x):
    return -2*x + exp(x)
    

def f7(x):
    return 3*x + 4*log(x) - 7

def fder7(x):
    return (4+3*x)/x
    

def f8(x):
    return (x**4) - 2*(x**2) + 4*x - 17

def fder8(x):
    return 4 - 4*x + 4*(x**3)


def f9(x):
    return exp(x) - 2*sin(x) - 7

def fder9(x):
    return -2*cos(x)+exp(x)


def f10(x):
    return log((x**2)+4)*exp(x) - 10

def fder10(x):
    return (4*log(4+x**2)*exp(x)+2*x*exp(x)+(x**2)*log(4+x**2)*exp(x))/(4+x**2)

print (Newton(f10,fder10,1.5, 1e-10, 5e4))

