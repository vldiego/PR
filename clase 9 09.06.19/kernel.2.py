#Kernel
############################

# Importando librerÃ­as
import numpy as np
import pandas as pd

# Ruta de trabajo

##path='C:/Users/Administrador.P1L2-PC06/Desktop/sesion09.06/'

#Importando data
##dataset=pd.read_csv(path+'Social_Network_Ads.csv')

dataset=pd.read_csv('Social_Network_Ads.csv')

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

#Componentes principales
from sklearn.decomposition import PCA
##como solo tengo 2 variables escojo 1
pca=PCA(n_components=1)
Xtrain_pca=pca.fit_transform(Xtrain_sc)
Xtest_pca=pca.transform(Xtest_sc)

#Discriminante linear
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda=LDA(n_components=1)
Xtrain_lda=lda.fit_transform(Xtrain_sc,ytrain)
Xtest_lda=lda.transform(Xtest_sc)

#Kernel PCA
from sklearn.decomposition import KernelPCA
kpca=KernelPCA(n_components=1,kernel='rbf')
Xtrain_kpca=kpca.fit_transform(Xtrain_sc)
Xtest_kpca=kpca.transform(Xtest_sc)

#Regresion Logistica
#######################
from sklearn.linear_model import LogisticRegression
##R.logistica es un algoritmo iterativo por eso usamos random_state para tener aprox 
##los mismos resultados
logistic=LogisticRegression(random_state=4)


#1) Variables originales
logistic.fit(Xtrain,ytrain)
logistic.score(Xtrain,ytrain)
logistic.score(Xtest,ytest)
##
#2) Variables estandarizadas
logistic.fit(Xtrain_sc,ytrain)
logistic.score(Xtrain_sc,ytrain)
logistic.score(Xtest_sc,ytest)

#3) Variables PCA
logistic.fit(Xtrain_pca,ytrain)
logistic.score(Xtrain_pca,ytrain)
logistic.score(Xtest_pca,ytest)

#4)
logistic.fit(Xtrain_lda,ytrain)
logistic.score(Xtrain_lda,ytrain)
logistic.score(Xtest_lda,ytest)

#5)
logistic.fit(Xtrain_kpca,ytrain)
logistic.score(Xtrain_kpca,ytrain)
logistic.score(Xtest_kpca,ytest)


