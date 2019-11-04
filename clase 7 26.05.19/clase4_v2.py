#Aplicacion: Analisis estadistico


#Importando librerias
import pandas as pd
import numpy as np

#Definiendo fichero de trabajo
path='C:/Users/Administrador.P1L2-PC08/Desktop/data/'

#Importando data


#Verificando informacion de la base de datos
notas1=pd.read_csv(path+'Notas1.csv',sep=';')
notas2=pd.read_csv(path+'Notas2.csv',sep=';')
notas3=pd.read_csv(path+'Notas3.csv',sep=';')
notas4=pd.read_csv(path+'Notas4.csv',sep=';')

# Append: concatenar

notas12=pd.concat([notas1,notas2])



notas34=pd.concat([notas3,notas4])

notas3.rename(columns={'ECONOMIA':'Economia','ECONOMETRIA':'Econometria'},inplace=True)


notas34=pd.concat([notas3,notas4])


# Uniendo base3 y base4
notas1234=pd.concat([notas12,notas34],axis=1)


notas1234=pd.merge(notas12,notas34,on='Estudiante',how='inner')


# Ordenar data
##############
#Por indices:
#por filas
df1=notas1234.sort_index(axis=0)
df1v=notas1234.sort_index(axis=0,ascending=False)
#por columnas
df2=notas1234.sort_index(axis=1)























