# Gestión de Bases de Datos
###########################


# Importando librerías
import numpy as np
import pandas as pd

# Definiendo nuestro fichero de trabajo
#path='E:/CTIC/Machine Learning/NUEVO/Sesion 02/'
path='C:/Users/Administrador.P1L2-PC06/Desktop/SESION2/'

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

notas1234['Promedio']=np.mean(notas1234, axis=1)

notas1234['Estado']=np.where(notas1234.Promedio>=15,'APROBADO','DESAPROBADO')
notas1234['Sexo']=['Masculino','Masculino','Femenino','Femenino','Femenino','Masculino']

df10=notas1234.groupby(['Sexo']).agg({'min','max','count'})
df11=notas1234.groupby(['Sexo'])['Algebra'].agg({'min','max','count'})

#Matrices de varianzas y coarianzas
notas1234

matriz_notas=notas1234[['Aritmetica','Algebra','Geomteria','Economia','Econometria']]

matriz_varcor=np.cov(matriz_notas,rowvar=False)

matriz_corr=np.corrcoef(matriz_notas,rowvar=False)

#Comando loc, se basa en el indice es decir, el nombre la fila
#y el nombre de la columna

notas1234.loc[3,'Geomteria']

notas1234.index=notas1234.Estudiante
notas1234
notas1234.loc['Laura','Geomteria']
notas1234.loc[['Laura','Jose'],['Aritmetica','Algebra']]
notas1234.loc['Melissa',:]

#Comando iloc, utiliza coordenadas

notas1234.iloc[1,4]
notas1234.iloc[1:3,2:4]


#Subsetting:
###########
#Un corchete es sintaxis de subseting y el otro corchete es
#sintaxis de seleccion de columnas

#Seleccion de columnas
notas1234[['Aritmetica','Algebra']]
notas1234.loc[:,['Aritmetica','Algebra']]

#Seleccion de filas
notas1234[2:5]
notas1234.iloc[2:5,:]
notas1234[notas1234.Aritmetica<15]

dframe=pd.DataFrame(notas1234)

#Eliminando columnas

dframe.drop(['Estudiante','Estado'],axis=1)

dframe.drop(['Estudiante','Estado'],axis=1,inplace=True)

#Eliminando filas
dframe.drop(['Jose','Melissa'],inplace=True)


#Duplicidad
#######################
notas=pd.read_csv(path+'Notas.csv',sep=';')

#Uniendo bases de datos

notas_dup=pd.merge(notas3,notas,on='Estudiante')

#Validando duplicados
sum(notas3.groupby(['Estudiante']).count()['Economia']>1)
sum(notas.groupby(['Estudiante']).count()['Aritmetica']>1)



#Eliminamos duplicados
######################
#Eliminando registros con todas las columnas iguales
notas.drop_duplicates(keep='first')
#Eliminando registros en base a una llave
notas.drop_duplicates(subset='Estudiante',keep='first')
#Eliminamos registros agrupando informacion
notas.groupby(['Estudiante']).mean()
notas.groupby(['Estudiante']).min()
notas.groupby(['Estudiante']).max()


































