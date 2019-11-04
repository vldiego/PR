#Aplicacion: Analisis estadistico


#Importando librerias
import pandas as pd
import numpy as np

#Definiendo fichero de trabajo
path='C:/Users/Administrador.P1L2-PC08/Desktop/Sesion01/'

#Importando data

ventas=pd.read_csv(path+'ventas.csv')

#Verificando informacion de la base de datos
ventas.columns

ventas.columns=['ventas','precio','public','calid','miss']
ventas.columns

ventas.drop(['miss'],axis=1,inplace=True)


#Analisis estadistico
ventas.describe()
resumen=ventas.describe()

#
#Covarianzas
#covarianza por columnas ya que asi estan las variables
ventas_cov=np.cov(ventas,rowvar=False)
#Correlaciones
ventas_cor=np.corrcoef(ventas,rowvar=False)

#Calculo de percentiles extremos: p1 p5 p95 p99
#Calculo de la asimetria y la kurtosis

#Prediccion

#1)Promedio

np.mean(ventas['ventas'])
#2)Mediana
np.percentile(ventas['ventas'],50)
#3) Correlacion entre ventas y publicidad
ventas.ventas/ventas.public
np.mean(ventas.ventas/ventas.public)
500*np.mean(ventas.ventas/ventas.public)
#4) Variaciones porcentuales
var_ventas=ventas.ventas.pct_change()
var_ventas.drop(0,inplace=True)
ventas.ventas.tail(1)*(1+np.mean(var_ventas))




