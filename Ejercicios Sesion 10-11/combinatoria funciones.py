# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:26:46 2021

@author: juana
"""
def titulo():
    print("Combinatoria de 2 numeros")
    
def combinatoria(m,n):
    comb= factorial(m) / factorial(n) * factorial(m-n)
    return comb

def factorial(n):
    factor=1
    for x in range(n):
        factor=factor*(n-x)
    return factor

titulo()
n1=int(input("Ingrese M: ")); n2=int(input("Ingrese N: "))
print(combinatoria(n1,n2))    