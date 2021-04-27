"""
TP4 - Ma123  -  M.Laurent BLETZACKER
Alexandre Jean-Philippe BESSON
Antony ABDEL MALAK

1-PT1
"""

from math import sin
from math import cos
from math import tan
from math import exp
from math import log
from math import acos
from math import atan
import matplotlib.pyplot as pp

def Dichotomie(f, a0, b0, epsilon, Nitermax):
    n=0
    a = a0
    b = b0
    nliste = []
    xn = []
    en = []

    while abs(b-a) > epsilon and n <= Nitermax:
        n += 1
        m = (a + b)/2

        nliste.append(n)
        xn.append(a)
        en.append(abs (b-a))

        if (f(a)*f(m) <= 0 ):
            b = m
        else:
            a = m
    return m, n, nliste, xn, en      
        

def Secante(f, x0, x1, epsilon, Nitermax):
    n=0
    a = x0
    b = x1
    nliste = []
    xn = []
    en = []

    while n <= Nitermax:
        x = b - ( b - a ) * f(b) / ( f(b) - f(a) )
        n += 1

        nliste.append(n)
        xn.append(x)
        en.append(abs(x-b))

        if abs (x - b) <= epsilon:
            return x, n, nliste, xn, en
        else:
            a, b = b, x

def PointFixe(g, x0, epsilon, Nitermax):
    n=0
    xold = x0
    erreur = g(xold)-xold
    nliste = []
    xn = []
    en = []

    while abs(erreur) > epsilon and n < Nitermax :
        xnew = g(xold)
        n += 1
        erreur = xnew - xold
        xold = xnew

        nliste.append(n)
        xn.append(xnew)
        en.append(abs(erreur))

    return xnew, n, nliste, xn, en

def Newton(f, fder, x0, epsilon, Nitermax):
    n=0
    xold = x0
    erreur = -(f(xold)/(fder(xold)))
    nliste = []
    xn = []
    en = []

    while abs(erreur) > epsilon and n < Nitermax :
        xnew = xold - f(xold)/fder(xold)
        n += 1
        erreur = xnew - xold
        xold = xnew

        nliste.append(n)
        xn.append(xnew)
        en.append(abs(erreur))

    return xnew, n, nliste, xn, en


def f0(x):
    return 2 * x - (1 + sin(x))

def fder0(x):
    return 2 - cos(x)


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
    


def g0(x):
    return (1 + sin(x))/2

def g1(x):
    return (9 - 3 * x)**(1/4)

def g2(x):
    return acos((x+2)/3)

def g3(x):
    return log(7/x)

def g4(x):
    return log(10 + x)

def g5(x):
    return atan((x + 5)/2)

def g6(x):
    return log((x**2) + 3)


def grapheList(liste1,liste2,liste3,liste4,liste5,liste6,liste7,liste8):
    pp.plot(liste1, liste2)
    pp.plot(liste3, liste4)
    pp.plot(liste5, liste6)
    pp.plot(liste7, liste8)
    pp.xlabel("n")
    pp.ylabel("erreur")
    pp.title("L'erreur en fonction du n pour chaque méthode")
    pp.show()
    
def graphesemilogList(liste1,liste2,liste3,liste4,liste5,liste6,liste7,liste8):
    pp.semilogy(liste1, liste2)
    pp.semilogy(liste3, liste4)
    pp.semilogy(liste5, liste6)
    pp.semilogy(liste7, liste8)
    pp.xlabel("n")
    pp.ylabel("erreur")
    pp.title("L'erreur en fonction du n pour chaque méthode")
    pp.show()
    




### Valeurs à modifier ###
valeur0 = 0
valeur1 = 0
valeur2 = 1
g = g0
fonction = f0
dérivée = fder0
#########################


xnew_fix, n_fix, nliste_fix, xn_fix, en_fix = PointFixe(g, valeur0, 1e-10, 5e4)
xnew_new, n_new, nliste_new, xn_new, en_new = Newton(fonction, dérivée, valeur0, 1e-10, 5e4)
m_dic, n_dic, nliste_dic, an_dic, en_dic = Dichotomie(fonction, valeur1, valeur2, 1e-10, 5e4)
x_sec, n_sec ,nliste_sec, xn_sec, en_sec = Secante(fonction, valeur1, valeur2, 1e-10, 5e4)


print ("Méthode du Point fixe :", 'alpha =', xnew_fix ,'et', n_fix, 'itérations')
print ("Méthode de Newton :", 'alpha =', xnew_new ,'et', n_new, 'itérations')
print ("Méthode de la Sécante :", 'alpha =', x_sec ,'et', n_sec, 'itérations')
print ("Méthode de la Dichotomie :", 'alpha =', m_dic ,'et', n_dic, 'itérations')

grapheList(nliste_fix, en_fix, nliste_new, en_new, nliste_sec, en_sec, nliste_dic, en_dic)
graphesemilogList(nliste_fix, en_fix, nliste_new, en_new, nliste_sec, en_sec, nliste_dic, en_dic)
