# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:38:56 2021

@author: juana
"""

dia=int(input("Ingrese el dia: "))
mes=int(input("Ingrese el mes: "))
año=int(input("Ingrese el año: "))

if dia < 30:
    print("El dia siguiente es: ",(dia+1),mes,año)
elif dia>30 and mes<=12:
    print("El dia siguiente es: ","1",(mes+1),año)
elif dia>30 and mes>12:
    print("El dia siguiente es: ","1","1",(año+1))    