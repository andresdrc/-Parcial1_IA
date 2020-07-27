# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:13:14 2020

@author: andres
"""


import pandas as pd
import numpy as np

df = pd.read_csv("alumno.csv")

media_prom = df["promedio"].mean()
mediana_prom = df["promedio"].median()
moda_prom = df["promedio"].mode()

media_edad = df["edad"].mean()
mediana_edad = df["edad"].median()
moda_edad = df["edad"].mode()

print("Promedio\nMedia: " +str(media_prom))
print("\nModa: " +str(moda_prom))

print("\nEdad\nMedia: " +str(media_edad))
print("\nModa: " +str(moda_edad))

 
#     Mediana: %d
#     Moda: %d
    
#     Edad 
#     Media: %d
#     Mediana: %d
#     Moda: %d
#     "
# """ %(media_prom,mediana_prom,moda_prom,media_edad,mediana_edad,moda_edad))
