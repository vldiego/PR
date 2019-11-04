# -*- coding: utf-8 -*-
"""
Created on Sun May 19 18:06:00 2019

@author: Administrador
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#media es 5, desviacion standar=2 (ojo no es varianza en python)
norm=np.random.normal(5,2,1000)



np.mean(norm)

np.max(norm)

np.var(norm)

np.std(norm)

np.median(norm)

#Importar libreria

from scipy.stats import kurtosis, skew

kurtosis(norm) #exceso de kurtosis

skew(norm) #asimetria

#Calculo de percentiles
np.percentile(norm,50)
np.percentile(norm,[5,15,25,50,75,85,95])
np.percentile(norm,50.5)
np.percentile(norm,range(101))


norm2=np.random.normal(30,15,1000)
norm2
np.percentile(norm,0)

#Percentiles 0,1,5,25,50,75,95,99,100
np.percentile(norm2,[0,1,5,25,75,95,99,100])

#Ejercicio: U ->N (u=30,std=15)

utilidad=np.random.normal(30,15,10000)
#Cual es la probabilidad de perdida
utilidad<=0
sum(utilidad<=0)
sum(utilidad<=0)/len(utilidad)

np.mean(utilidad<=0)

#Cual es la probabilidad que la utilidad este entre 20 y 40

(utilidad<=40)&(utilidad>=25)
sum((utilidad<=40)&(utilidad>=25))
sum((utilidad<=40)&(utilidad>=25))/len(utilidad)

np.percentile(utilidad,[0,1,5,25,50,75,95,99,100])

#Calcular x0 si P(U<=x0)=0.1%

np.percentile(utilidad,0.1)

#Semilla aleatoria
np.random.uniform()
np.random.seed(4)
np.random.uniform()







