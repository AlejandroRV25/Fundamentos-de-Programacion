# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:20:09 2021

@author: juana
"""

x= float(input("Ingrese el primer dato: "))
y= float(input("Ingrese el segundo dato: "))
z= float(input("Ingrese el tercer dato: "))
if y>x and x>z:
    print("El número central es: ",x)
elif z>x and x>y:
    print("El número central es: ",x)
elif x>y and y>z:
    print("El número central es: ",y)
elif z>y and y>x:
    print("El número central es: ",y)
elif x>z and z>y:
    print("El número central es: ",z)
elif y>z and z>x:
    print("El número central es: ",z)
elif x==y and x==z:
    print("Los números no pueden ser iguales")
    