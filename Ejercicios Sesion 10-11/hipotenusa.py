# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:16:59 2021

@author: juana
"""
import math

ve_cateto1= 0.0
ve_cateto2= 0.0 

def ftitulo():
    print("CALCULO DE LA HIPOTENUSA DE UN TRIANGULO RECTANGULO")


def f_calcularhipotenusa(p_cateto1,p_cateto2):


    vps_hipotenusa= 0.0
   

    vp_radicando=math.sqrt(math.pow(p_cateto1,2) + math.pow(p_cateto2,2))
    vps_hipotenusa= vp_radicando


    return vps_hipotenusa 
def f_despedida():
    print("--ADIOS--")

ftitulo()  
ve_cateto1=int(input("Ingrese el cateto uno: "))
ve_cateto2=int(input("Ingrese el cateto dos: "))
vps_rf_hip=f_calcularhipotenusa(ve_cateto1,ve_cateto2)
print("La hipotenusa es: ",vps_rf_hip)

ve_cateto1=int(input("Ingrese el cateto uno: "))
ve_cateto2=int(input("Ingrese el cateto dos: "))
vps_rf_hip=f_calcularhipotenusa(ve_cateto1,ve_cateto2)
print("La hipotenusa es: ",vps_rf_hip)
f_despedida()

