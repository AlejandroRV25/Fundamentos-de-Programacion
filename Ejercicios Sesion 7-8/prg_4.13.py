# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:13:00 2021

@author: juana
"""

contador_rep=0
while contador_rep < 1:
    print("""
          1.Enero
          2.Febrero
          3.Marzo
          4.Abril
          5.Mayo
          6.Junio
          7.Julio
          8.Agosto
          9.Septiembre
          10.Octubre
          11.Noviembre
          12.Diciembre
          """)
    mes=int(input("Ingrese el mes:"))
    
    if mes == 1:
        dia=int(input("Ingrese el dia: "))
        if dia > 31: 
            print("Enero solo tiene 31 dias")
    elif mes == 2:
        dia=int(input("Ingrese el dia: "))
        if dia > 29: 
            print("Febrero solo tiene 29 dias")
    elif mes == 3:
        dia=int(input("Ingrese el dia: "))
        if dia > 31: 
            print("Marzo solo tiene 31 dias")
    elif mes == 4:
        dia=int(input("Ingrese el dia: "))
        if dia > 30: 
            print("Abril solo tiene 31 dias")
    elif mes == 5:
        dia=int(input("Ingrese el dia: "))
        if dia > 31: 
            print("Mayo solo tiene 31 dias")
    elif mes == 6:
        dia=int(input("Ingrese el dia: "))
        if dia > 30: 
            print("Junio solo tiene 31 dias")
    elif mes == 7:
        dia=int(input("Ingrese el dia: "))
        if dia > 31: 
            print("Julio solo tiene 31 dias")
    elif mes == 8:
        dia=int(input("Ingrese el dia: "))
        if dia > 31: 
            print("Agosto solo tiene 31 dias")
    elif mes == 9:
        dia=int(input("Ingrese el dia: "))
        if dia > 30: 
            print("Septiembre solo tiene 31 dias")
    elif mes == 10:
        dia=int(input("Ingrese el dia: "))
        if dia > 31: 
            print("Octubre solo tiene 31 dias")
    elif mes == 11:
        dia=int(input("Ingrese el dia: "))
        if dia > 30: 
            print("Noviembre solo tiene 31 dias")
    elif mes == 12:
        dia=int(input("Ingrese el dia: "))
        if dia > 31: 
            print("Diciembre solo tiene 31 dias")
            
    else:
        print("Un año solo tiene 12 meses")
                    
    contador_rep=contador_rep+1   
    
if dia < 31:
    print("dia",dia,"-","mes",mes)

else:
    print("Los datos ingresados no son correctos")
    
        
            