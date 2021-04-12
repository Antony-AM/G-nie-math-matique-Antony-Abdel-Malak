# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:10:07 2021

@author: Antony Abdel Malak
"""


#exercice 1

from math import sin 

x=0

def g(x):
    return (1+sin(x))/2

for n in range (0,41):
    x=g(x)

print("La valeur x =",x,"pour n =",n)


print("") #pour la beauté du résultat

#exercice 2

epsilon = 1e-8
a = 2*x
b = sin(x)+1

if (a-b) < epsilon:
    print("x(40) est bien la bonne solution")
else :
    print("x(40) n'est pas la bonne solution")
    
print("")
    
#exercice 3
alpha = x
k = 1/2
x=0
for n in range(0,41):
    x=g(x)
    en = abs(x-alpha)
    M = k**n
    
    print("n =",n,"| x(n) =| en =",en, "| Mn =",M)
    if en <= M:
        print("en est majorée")
    else:
        print("en n'est pas majorée")