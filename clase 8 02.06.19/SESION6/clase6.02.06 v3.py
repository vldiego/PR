# Importando librerÃ­as
import numpy as np
import pandas as pd


#Generando data frame

df=pd.DataFrame([[1,np.nan,2,np.nan],[2,3,5,np.nan],[np.nan,4,6,np.nan]])

#Asignando nombres a las columnas
df.columns=['x1','x2','x3','x4']
#Asignando nombres a las filas
df.index=['a','b','c']

df
#Contando valores en missing
############################
#Para toda la base
df.isnull() #base total
np.sum(df.isnull()) #missing por columnas
np.sum(df.isnull(),axis=1) #missing por filas
#Para una columna
df.isnull()['x2']
df['x2'].isnull()
sum(df.isnull()['x2'])
sum(df.isnull()['x2'])/len(df)
#Para una fila
df.isnull()[df.index=='b']
df[df.index=='b'].isnull()
df.loc['b',:].isnull()
np.sum(df[df.index=='b'].isnull(),axis=1)
np.sum(df[df.index=='b'].isnull(),axis=1)/df.shape[1]

#Tratamiento de missings
#######################
# I) Eliminando observaciones
#########################
df
df.dropna() #Elimina todas las filas o columnas que tengan algun missing
df.dropna(axis=1) #columnas
df.dropna(axis=0) #filas

#Eliminando filas o columnas donde todo este en missing
df.dropna(how='all',axis=0) #filas
df.dropna(how='all',axis=1) #columnas

#Estableciendo umbrales para los datos poblados
df.dropna(thresh=2,axis=0) #filas
df.dropna(thresh=2,axis=1) #columnas


#Asignando valores
df.fillna(0)
df.x1.fillna(0)
df.x2.fillna(9999)

df.x2.fillna(np.mean(df.x2))
df

#Completar con el valor previo
df.fillna(method='bfill',axis=0) #columnas
df.fillna(method='bfill',axis=1) #filas

#Tratamiento de outliers
########################
import matplotlib.pyplot as plt
norm=np.random.normal(5000,125,size=1000)
plt.hist(norm)
df2=pd.DataFrame(norm)
#Calculando percentiles
perc=np.percentile(norm,[1,99])
df2.columns=['norm']

#Acotando
df2['norm_acot']=np.where(df2.norm<=perc[0],perc[0],
   np.where(df2.norm>=perc[1],perc[1],df2.norm))

df2.describe()















