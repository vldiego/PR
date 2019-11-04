# Gestión de Bases de Datos
###########################


# Importando librerías
import numpy as np
import pandas as pd

# Definiendo nuestro fichero de trabajo
path='E:/CTIC/Machine Learning/NUEVO/Sesion 02/'

# Importando data
notas1=pd.read_csv(path+'Notas1.csv',sep=';')
notas2=pd.read_csv(path+'Notas2.csv',sep=';')
notas3=pd.read_csv(path+'Notas3.csv',sep=';')
notas4=pd.read_csv(path+'Notas4.csv',sep=';')

# Append: Concatenar
notas12=pd.concat([notas1,notas2])
notas34=pd.concat([notas3,notas4])
# Renombrando variables
notas3.rename(columns={'ECONOMIA':'Economia',
                       'ECONOMETRIA':'Econometria'},
inplace=True)
# Generando nuevamente el cruce
notas34=pd.concat([notas3,notas4])

# Uniendo base3 y base4
notas1234=pd.concat([notas12,notas34],axis=1)
# Merge: Uniendo bases de manera adecuada
notas1234=pd.merge(notas12,notas34,on='Estudiante',
                   how='inner')

# Ordenar data
###############
# Por índices:
# por filas
df1=notas1234.sort_index(axis=0)
# por columnas
df2=notas1234.sort_index(axis=1)

# Por una columna en particular
# creciente: de menor a mayor
df3=notas1234.sort_values(by='Algebra')
# decreciente: de mayor a menor
df4=notas1234.sort_values(by='Algebra',
                          ascending=False)













































