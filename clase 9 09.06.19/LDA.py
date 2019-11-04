#Discriminante lineal
############################

# Importando librerÃ­as
import numpy as np
import pandas as pd

# Ruta de trabajo

path='C:/Users/Administrador.P1L2-PC06/Desktop/sesion09.06/'

#Importando data
dataset=pd.read_csv(path+'Social_Network_Ads.csv')

#Generando variables X e y
X=dataset.iloc[:,[2,3]].values
y=dataset.iloc[:,4].values

#Separando en train y test
from sklearn.model_selection import train_test_split
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,
                                           random_state=4)

#Aplicando Estandarizacion
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
Xtrain_sc=sc.fit_transform(Xtrain)
Xtest_sc=sc.transform(Xtest)

#Discriminante lineal
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

#Contar Categorias
dataset['Purchased'].value_counts()

#Aplicando LDA
lda=LDA(n_components=1)
Xtrain_lda=lda.fit_transform(Xtrain_sc,ytrain)
## solo transform porque ya aprendio en el anterior
Xtest_lda=lda.transform(Xtest_sc)
#Coeficientes
coeficientes=lda.coef_
