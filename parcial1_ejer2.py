# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:19:46 2020

@author: andres
"""

from sklearn import preprocessing

from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np


df = pd.read_csv("alumno.csv")

datos = df[["promedio","edad"]]
print("datos de promedio y edad: \n"+ str(datos)+ "\n")

imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(datos)
datos_llenos = imp.transform(datos)
#PREPROCESAMIENTO COMPLETAR DATOS NaN
print("datos completos: \n" + str(datos_llenos) + "\n")

#PREPROCESAMIENTO NORMALIZACION DE DATOS
nor = preprocessing.Normalizer(norm='l2',copy=True).fit_transform(datos_llenos)
print("datos normalizados: \n" + str(nor))  

