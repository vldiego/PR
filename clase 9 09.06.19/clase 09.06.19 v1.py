# Definiendo nuestro fichero de trabajo

path='C:/Users/Administrador.P1L2-PC06/Desktop/sesion09.06/'


# Importando librerÃ­as
import numpy as np
import pandas as pd

#Cargando base de datos
data=pd.read_csv(path+'caso.csv')
X=data.loc[:,['atraso','casa','edad','dias_lab','exp_sf',
           'nivel_ahorro','ingreso','linea_sf','deuda_sf',
           'zona','clasif_sbs','nivel_educ']]

y=data.loc[:,'mora']

#Division en train y test
from sklearn.model_selection import train_test_split
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,random_state=4)

#Descriptivo rapido
#####################
data.describe()
data.info()
data.casa.value_counts()
data.casa.value_counts()/len(data)
#otra forma
data.casa.value_counts()/data.shape[0]
#Analizando duplicados
######################
data.id.value_counts()
data.id.value_counts()>1
sum(data.id.value_counts()>1)
#Como la suma es 0 -> NO HAY DUPLICADOS



#Analizando valores extremos
###########################

#Analizando percentiles omitiendo missings
np.percentile(Xtrain.edad,[0,1,5,95,99,100])
##si sale error es que hay valores missings
np.percentile(Xtrain.deuda_sf,[0,1,5,95,99,100])
##Analizando los datos sin missings en deuda_sf
a=np.percentile(Xtrain[-Xtrain.deuda_sf.isnull()]['deuda_sf'],
                     [0,1,5,95,99,100])
#Asignando cotas superiores
Xtrain.loc[Xtrain.edad>=63,'edad']=63 #(p99 de la edad)
Xtrain.loc[Xtrain.deuda_sf>=28984.539,'deuda_sf']=28984.539 #(p95)
#Asignando cotas inferiores
Xtrain.loc[Xtrain.edad<=21,'edad']=21 #p1
Xtrain.loc[Xtrain.deuda_sf<=0,'deuda_sf']=0

#Verificando
min(Xtrain.edad),min(Xtrain.deuda_sf)
max(Xtrain.edad),min(Xtrain.deuda_sf)


#Analizando missings
##########################
#Cuantificando valores faltantes
np.sum(Xtrain.isnull(),axis=0)
#Analizando valores a asignar
data_asig=Xtrain[['exp_sf','linea_sf','deuda_sf']].describe()
#Asignando missings
Xtrain.exp_sf.fillna(28,inplace=True)
Xtrain.linea_sf.fillna(0,inplace=True)
Xtrain.deuda_sf.fillna(0,inplace=True)
#Verificando
np.sum(Xtrain.isnull(),axis=0)

#Transformaciones
##################

#Tratamiento de variables categoricas

#Caso: asignando OR
data_train=pd.concat([ytrain,Xtrain],axis=1)
or_casa=pd.DataFrame(data_train.groupby(['casa']).mean()['mora'])
or_casa['OR']=(1-or_casa['mora'])/or_casa['mora']
Xtrain['casa_f']=np.where(Xtrain.casa=='Alquilada',0.5,
      np.where(Xtrain.casa=='FAMILIAR',0.376174,
               np.where(Xtrain.casa=='OTRAS',0,178571,0.558743)))

data_train.groupby('casa').mean()
data_train.casa

#Nivel educativo: Dummies
Xtrain.nivel_educ.value_counts()
base_dummy=pd.get_dummies(Xtrain['nivel_educ'],prefix='d')
Xtrain=pd.concat([Xtrain,base_dummy],axis=1)

#Clasificacion SBS y zona: Agrupaciones
Xtrain.clasif_sbs.value_counts()
Xtrain.zona.value_counts()

Xtrain['zona_f']=np.where(Xtrain.zona=='Lima',1,0)
Xtrain['clasif_sbs_f']=np.where(Xtrain.clasif_sbs==0,1,0)

#Eliminando variables que no se utilizaran
Xtrain.drop(['casa','nivel_educ','zona','clasif_sbs'],axis=1,
            inplace=True)





































