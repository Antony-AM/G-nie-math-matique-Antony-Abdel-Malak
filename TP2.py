# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:25:05 2021

@author: anton
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


def PointFixe(g, x0, epsilon, Nitermax):
    n=0
    xold = x0
    erreur = g(xold)-xold

    while abs(erreur) > epsilon and n < Nitermax :
        xnew = g(xold)
        n += 1
        erreur = xnew - xold
        xold = xnew
        print(n,xnew)
    return xnew




def g0(x):
    return (1 + sin(x))/2

def g1_1(x):
    return (9 - x**4) / 3

def g1_2(x):
    return (9 - 3 * x)**(1/4)

def g2_1(x):
    return 3 * cos(x) - 2

def g2_2(x):
    return acos((x+2)/3)

def g3_1(x):
    return log(7/x)

def g3_2(x):
    return 7/exp(x)

def g4_1(x):
    return exp(x) - 10

def g4_2(x):
    return log(10 + x)

def g5_1(x):
    return 2 * tan(x) - 5

def g5_2(x):
    return atan((x + 5)/2)

def g6_1(x):
    return log((x**2) + 3)

def g6_2(x):
    return sqrt(exp(x)-3)

def g7_1(x):
    return (7 - 4 * log(x))/3

def g7_2(x):
    return exp((7-3*x)/4)

def g8_1(x):
    return (2*(x**2) + 4*x + 17)**(1/4)

def g8_2(x):
    return sqrt((x**4 + 4*x - 17)/2)

def g8_3(x):
    return (-(x**4) + 2*(x**2) + 17)/4 

def g9_1(x):
    return log(2 * sin(x) + 7)

def g9_2(x):
    return asin((exp(x) - 7)/2)

def g10_1(x):
    return sqrt(exp(10/exp(x)) - 4)

def g10_2(x):
    return log(10/log((x**2) + 4))





print (PointFixe(g1_1,0.25, 1e-10, 5e4))

