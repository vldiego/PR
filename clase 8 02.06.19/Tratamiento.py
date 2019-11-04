# Trabajando con valores missing
################################

# Importando librerías
import pandas as pd
import numpy as np

# Generando data frame
df=pd.DataFrame([[1,np.nan,2,np.nan],
                 [2,3,5,np.nan],
                 [np.nan,4,6,np.nan]])
# Asignando nombres a las columnas
df.columns=['x1','x2','x3','x4']
# Asignando nombres a las filas
df.index=['a','b','c']

# Contando valores en missing
##############################
# Toda la base
df.isnull() # base total
np.sum(df.isnull()) # missing por columnas
np.sum(df.isnull(),axis=1) # missing por filas
# Para una columna
df.isnull()['x2']
df['x2'].isnull()
sum(df.isnull()['x2'])
sum(df.isnull()['x2'])/len(df)
sum(df.isnull()['x2'])/df.shape[0]
# Para una fila
df.isnull()[df.index=='b']
df[df.index=='b'].isnull()
df.loc['b',:].isnull()
np.sum(df[df.index=='b'].isnull(),axis=1)
np.sum(df[df.index=='b'].isnull(),axis=1)/df.shape[1]

# Tratamiento de missings
#########################
# 1) Elimiando observaciones
############################
df
# Elimina todas las filas o columnas con al menos 1 missing
df.dropna(axis=1) # columnas
df.dropna(axis=0) # filas

# Eliminando filas o columnas donde todo este en missing
df.dropna(how='all',axis=0) # filas
df.dropna(how='all',axis=1) # columnas

# Estableciendo umbrales para los datos poblados
df.dropna(thresh=2,axis=0) # filas
df.dropna(thresh=2,axis=1) # columnas

# 2) Asignando valores
df
df.fillna(0)
df.x1=df.x1.fillna(0)
df.x2=df.x2.fillna(9999)
df

# Restaurando data frame
df=pd.DataFrame([[1,np.nan,2,np.nan],
                 [2,3,5,np.nan],
                 [np.nan,4,6,np.nan]])
# Asignando nombres a las columnas
df.columns=['x1','x2','x3','x4']
# Asignando nombres a las filas
df.index=['a','b','c']

df.x2=df.x2.fillna(np.mean(df.x2))
df

# Completar con el dato previo
df.fillna(method='ffill',axis=0) # columnas
df.fillna(method='ffill',axis=1) # filas

# Completar con el valor siguiente
df.fillna(method='bfill',axis=0) # columnas
df.fillna(method='bfill',axis=1) # filas

# Tratamiento de outliers
#########################
import matplotlib.pyplot as plt
norm=np.random.normal(5000,125,size=1000)
plt.hist(norm)
df2=pd.DataFrame(norm)
# Calculando percentiles
perc=np.percentile(norm,[1,99])
df2.columns=['norm']

# Acotando
df2['norm_acot']=np.where(df2.norm<=perc[0],perc[0],
   np.where(df2.norm>=perc[1],perc[1],df2.norm))
df2.describe()

# Eliminando
df3=df2[(df2.norm>=perc[0])&(df2.norm<=perc[1])]
[df3.shape[0],df2.shape[0]]

































































