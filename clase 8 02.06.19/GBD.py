# Gestión de BBDD
#################

# Importando librerías
import numpy as np
import pandas as pd

# Definendo ruta de trabajo
path='C:/Users/AdminCTIC/Desktop/GBD/'

# Importando data
notas1=pd.read_csv(path+'Notas1.csv',sep=';')
notas2=pd.read_csv(path+'Notas2.csv',sep=';')
notas3=pd.read_csv(path+'Notas3.csv',sep=';')
notas4=pd.read_csv(path+'Notas4.csv',sep=';')

# Uniendo información
notas3.rename(columns={'ECONOMIA':'Economia',
                       'ECONOMETRIA':'Econometria'},
inplace=True)

notas12=pd.concat([notas1,notas2])
notas34=pd.concat([notas3,notas4])
notas1234=pd.merge(notas12,notas34,on='Estudiante',
                   how='inner')

# Ordenando data
################
# Por indices
df1=notas1234.sort_index(axis=0) # por filas
df2=notas1234.sort_index(axis=1) # por columnas

# Por una columna en particular
df3=notas1234.sort_values(by='Algebra') # creciente
df4=notas1234.sort_values(by='Algebra',
                          ascending=False) # decreciente

# Comando head y tail
df5=notas1234.head() # muestra 5 primeros registros
df6=notas1234.head(1) # muestra primer registro
df7=notas1234.tail() # muestra 5 ultimos registros
df8=notas1234.tail(1) # muestra ultimo registro

# Ejemplos:
#¿Qué estudiante tiene mayor nota de Econometria?
notas1234.sort_values(by='Econometria').tail(1)['Estudiante']
notas1234[notas1234.Econometria==max(notas1234.Econometria)]['Estudiante']
#¿Qué estudiante tiene menor nota de Aritmetica?
notas1234.sort_values(by='Aritmetica').head(1)['Estudiante']
#¿Cuales son los 3 priumeros puestos del aula?
np.mean(notas1234) # promedio por columnas
np.mean(notas1234,axis=1) # promedio por filas
notas1234['Promedio']=np.mean(notas1234,axis=1)
notas1234.sort_values(by='Promedio').tail(3)['Estudiante']

# Generando nuevas variables
notas1234['Estado']=np.where(notas1234.Promedio>=15,'Aprobado',
         'Desaprobado')
notas1234['Sexo']=['Masculino','Masculino','Femenino','Femenino',
         'Femenino','Masculino']

# Agrupando por variable Sexo
df9=notas1234.groupby(['Sexo']).mean()
df9=notas1234.groupby(['Sexo']).max()
df9=notas1234.groupby(['Sexo']).min()
df9=notas1234.groupby(['Sexo']).std()
df9=notas1234.groupby(['Sexo']).median()

#Function	Description
#count	Number of non-null observations
#sum	Sum of values
#mean	Mean of values
#mad	Mean absolute deviation
#median	Arithmetic median of values
#min	Minimum
#max	Maximum
#mode	Mode
#abs	Absolute Value
#prod	Product of values
#std	Unbiased standard deviation
#var	Unbiased variance
#sem	Unbiased standard error of the mean
#skew	Unbiased skewness (3rd moment)
#kurt	Unbiased kurtosis (4th moment)
#quantile	Sample quantile (value at %)
#cumsum	Cumulative sum
#cumprod	Cumulative product
#cummax	Cumulative maximum
#cummin	Cumulative minimum

df10=notas1234.groupby(['Sexo']).agg({'min','max','count'})
df11=notas1234.groupby(['Sexo'])['Algebra'].agg({'min','max','count'})
df12=notas1234.groupby(['Sexo'])['Algebra'].agg({'minimo':'min',
                      'maximo':'max','numero':'count'})

# Matriz de varianzas y covarianzas
matriz_notas=notas1234[['Aritmetica','Algebra',
                        'Geomteria','Economia',
                        'Econometria']]
matriz_varcov=np.cov(matriz_notas,rowvar=False)
# si rowvar=True (default), es covarianzas por filas

# Matriz de correlaciones
matriz_corr=np.corrcoef(matriz_notas,rowvar=False)

# Comando loc
notas1234.loc[3,'Geomteria']
notas1234.index=notas1234.Estudiante
notas1234.loc['Laura','Geomteria']
notas1234.loc[['Laura','Jose'],['Aritmetica','Algebra']]
notas1234.loc['Melissa',:]

# Comando iloc
notas1234.iloc[1,4]
notas1234.iloc[1:3,2:4]

# Subsetting:
############

# Seleccion de columnas
notas1234[['Aritmetica','Algebra']]
notas1234.loc[:,['Aritmetica','Algebra']]

# Seleccion de filas
notas1234[2:5]
notas1234.iloc[2:5,:]
notas1234[notas1234.Aritmetica<15]

dframe=pd.DataFrame(notas1234)
# Eliminando columnas
dframe.drop(['Estudiante','Estado'],axis=1,
            inplace=True)
# Eliminando filas
dframe.drop(['Jose','Melissa'],inplace=True)

# Duplicados
#############
notas=pd.read_csv(path+'Notas.csv',sep=';')

# Uniendo bases de datos
notas_dup=pd.merge(notas3,notas,on='Estudiante')

# Validando duplicados
sum(notas3.groupby(['Estudiante']).count()['Economia']>1)
sum(notas.groupby(['Estudiante']).count()['Aritmetica']>1)

str='Avión'
str=str.lower()
str=str.replace('ó','o')
str

# Eliminando duplicados
#######################
# Eliminando registros con todas las columnas iguales
notas.drop_duplicates(keep='first')
# Eliminando registros en base a una llave
notas.drop_duplicates(subset='Estudiante',keep='first')
# Eliminando registros agrupando informacion
notas.groupby(['Estudiante']).max()
notas.groupby(['Estudiante']).min()
notas.groupby(['Estudiante']).mean()





































































































































