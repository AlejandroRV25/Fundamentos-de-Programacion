# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:05:28 2021

@author: juana
"""

def ordenar_imprimir(n1,n2,n3):
    if n1<n2 and n1<n3:
        if (n2<n3):
            print(n1,n2,n3)
        else:
            print(n1,n3,n2)
    else:
        if (n2<n3):
            if (n1<n3):
                print(n2,n1,n3)
            else:
                print(n2,n3,n1)
        else:
            if (n1<n2):
                print(n3,n1,n2)
            else:
                print(n3,n2,n1)
            

def cargar():
    num1=int(input("Ingrese primer valor:"))
    num2=int(input("Ingrese segundo valor:"))
    num3=int(input("Ingrese tercer valor:"))
    ordenar_imprimir(num1,num2,num3)

    
# bloque principal

cargar()