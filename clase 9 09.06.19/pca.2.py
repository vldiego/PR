# Importando librerÃ­as
import numpy as np
import pandas as pd

# Ruta de trabajo

path='C:/Users/Administrador.P1L2-PC06/Desktop/sesion09.06/'

#Importando data
#--dataset=pd.read_csv(path+'Wine.csv')
dataset=pd.read_csv('Wine.csv')
#Descriptivos
dataset.describe()

#Generando variables
X=dataset.iloc[:,0:13].values
y=dataset.iloc[:,13].values

#Separando base en train y test
from sklearn.model_selection import train_test_split
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,
                                           random_state=4)



#Estandarizacion
#####################
#Descangando librerias
from sklearn.preprocessing import StandardScaler


#Generando objeto
sc=StandardScaler()


#Entrenando y aplicando
Xtrain_sc=sc.fit_transform(Xtrain)

'''
#Otra forma

Xtrain_sc2=StandardScaler().fit_transform(Xtrain)

'''
#Aplicando lo aprendido (Prediccion)

Xtest_sc=sc.transform(Xtest)
#Revisar lo aprendido

##Indica la media de X_train, ya que ha aprendido su media
sc.mean_
##Indica la varianza de X_train, ya que ha aprendido su media
sc.var_

#####
#Fit: aprender los parametros
#Transform: utiliza los paramentros
#####

#Aplicando componentes principales
from sklearn.decomposition import PCA

pca=PCA(n_components=13)#Objeto
Xtrain_pca=pca.fit_transform(Xtrain_sc) #Entrenando y aplicando
Xtest_pca=pca.transform(Xtest_sc) #Aplicando lo aprendido

#Coeficientes de los componentes
componentes=pca.components_
#Verificando
verificando=np.sum(componentes**2,axis=0)

#Varianza de los componentes
var_explicada=pca.explained_variance_
ratio_var_exp=pca.explained_variance_ratio_

#Analizando correlaciones
correl=np.corrcoef(Xtrain_sc,rowvar=False)
correl_pca=np.corrcoef(Xtrain_pca,rowvar=False)

#Vamos a quedarnos con los tres principales componentes
pca=PCA(n_components=3) #Objeto
