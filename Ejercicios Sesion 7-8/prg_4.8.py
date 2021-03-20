# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:23:52 2021

@author: juana
"""

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
if(a % b==0):
 print(str(b)+" es divisor de "+str(a))
else:
 if(b%a==0):
  print(str(a)+" es divisor de "+str(b))
 else:
  print("N1inguno es divisor del otro")