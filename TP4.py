from math import sin
from math import cos
from math import tan
from math import exp
from math import log
from math import acos
from math import atan
from math import asin
from math import sqrt



def Dichotomie(f, a0, b0, epsilon, Nitermax):
    n=0
    a = a0
    b = b0

    while abs(b-a) > epsilon and n <= Nitermax:
        n += 1
        m = (a + b)/2
        if (f(a)*f(m) <= 0 ):
            b = m
        else:
            a = m
    return(m,n)        
        

def Secante(f, x0, x1, epsilon, Nitermax):
    n=0
    a = x0
    b = x1
    while n <= Nitermax:
        x = b - ( b - a ) * f(b) / ( f(b) - f(a) )
        n += 1
        
        if abs (x - b) <= epsilon:
            return x, n
        else:
            a, b = b, x





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

print ("Méthode de la Sécante :", Secante(f1, 1, 2, 1e-10, 5e4))
print ("Méthode de la Dichotomie", Dichotomie(f1, 1, 2, 1e-10, 5e4))