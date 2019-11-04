#Aplicacion: Analisis estadistico


#Importando librerias
import pandas as pd
import numpy as np

#Definiendo fichero de trabajo
path='C:/Users/Administrador.P1L2-PC08/Desktop/Sesion01/'

#Importando data

data=pd.read_csv(path+'ventas.csv')

#Verificando informacion de la base de datos
data.columns

data.columns=['ventas','precio','public','calid','miss']
data.columns

data.drop(['miss'],axis=1,inplace=True)

from statsmodels.formula.api import ols


modelo_mco=ols(formula='ventas~precio+public+calid',data=data)

modelo_mco=modelo_mco.fit()

modelo_mco.summary()

#Extrayendo coeficientes
modelo_mco.params

#Extrayendo desviaciones estandar
modelo_mco.bse

#Prueba de hipotesis

# Ho: bcalid=2

#Definir parametros
k=2 #valor a testear
alpha=0.05 #Nivel de significancia
#Estadistico calculado
tcalc=(modelo_mco.params[3]-k)/modelo_mco.bse[3]
tcalc

#Estadistico de tablas
from scipy import stats

ttab=stats.t.ppf(alpha/2,len(data)-len(modelo_mco.params))

#Regla de decision

if abs(tcalc)>abs(ttab):
    print('Se rechaza la Ho')
else:
    print('No se rechaza la Ho')
    
    
    
    
# Ho: bpublicidad=0
k=2 #valor a testear
alpha=0.05 #Nivel de significancia
#Estadistico calculado
tcalc=(modelo_mco.params[2]-k)/modelo_mco.bse[2]
ttab=stats.t.ppf(alpha/2,len(data)-len(modelo_mco.params))

#Regla de decision

if abs(tcalc)>abs(ttab):
    print('Se rechaza la Ho')
else:
    print('No se rechaza la Ho')
#La respuesta es: se rechaza la Ho
#Por lo tanto beta2 es igual a cero. es decir la publicidad impacta en las ventas
    
######me sale incorrecto

    
# Ho: bpublicidad<=0
k=2 #valor a testear
alpha=0.05 #Nivel de significancia
#Estadistico calculado
tcalc=(modelo_mco.params[2]-k)/modelo_mco.bse[2]
ttab=stats.t.ppf(1-alpha,len(data)-len(modelo_mco.params))


#Regla de decision

if tcalc>ttab:
    print('Se rechaza la Ho')
else:
    print('No se rechaza la Ho')

#####################

##Generando intervalo de confianza IC(bprecio)


ttab=stats.t.ppf(1-alpha/2,len(data)-len(modelo_mco.params))
tcalc=(modelo_mco.params[2]-k)/modelo_mco.bse[2]

lsup_bprecio=modelo_mco.params[1]+ttab*modelo_mco.bse[1]
linf_bprecio=modelo_mco.params[1]-ttab*modelo_mco.bse[1]
print('El intervalo de confianza de b1 es:[',
                                           linf_bprecio,'-',
                                           lsup_bprecio,
                                           ']')
#Prediccion
data['ventas_est']=modelo_mco.predict(data)

data['ventas_est2']=modelo_mco.params[0]+\
modelo_mco.params[1]*data['precio']+\
modelo_mco.params[2]*data['public']+\
modelo_mco.params[3]*data['calid']






































