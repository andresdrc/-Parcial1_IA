# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:11:17 2020

@author: andres
"""

import csv
import math

masc = 0
fem = 0 
mediaProm = 0
mediaEdad = 0
sumaEdad = 0
sumaProm = 0
contador = 0

sumatoriaProm = 0
sumatoriaEdad = 0

archivo = open("alumnoUno.csv")
reader = csv.reader(archivo,delimiter=",")

for linea in reader:
    print(linea[0]+"\t" +linea[1]+"\t"+linea[2]+"\t"+linea[3]
          +"\t"+linea[4]+"\t"+linea[5])
    sumatoriaProm += pow(int(linea[4])-mediaProm,2)
    sumatoriaEdad += pow(int(linea[4])-mediaProm,2)    
    contador += 1
    sumaEdad += int(linea[5])
    sumaProm += int(linea[4])
    
    


    
mediaEdad = sumaEdad/contador
mediaProm = sumaProm/contador

print("Media de edad: " + str(mediaEdad))
print("Media de promedio: " + str(mediaProm))

for linea in reader:
    print("linea: " + linea[4])

deprom = math.sqrt(sumaProm/contador)
print("Desviacion estandar del promedio: " + str(deprom))


deEdad = math.sqrt(sumaEdad/contador)
print("Desviacion estandar de la edad: " + str(deEdad))










