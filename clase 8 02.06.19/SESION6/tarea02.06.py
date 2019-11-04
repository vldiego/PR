# Importando librerÃ­as
import numpy as np
import pandas as pd

# Definiendo nuestro fichero de trabajo

path='C:/Users/Administrador.P1L2-PC06/Desktop/SESION6/'

# Importando data

country=pd.read_csv(path+'countryGDP.csv',sep=',')
happy=pd.read_csv(path+'happy2015.csv',sep=',')
engange=pd.read_csv(path+'endangeredLang.csv',sep=',')
Global=pd.read_csv(path+'GlobalFirePower.csv',sep=',')


country.drop_duplicates(keep='first')
happy.drop_duplicates(keep='first')
engange.drop_duplicates(keep='first')
Global.drop_duplicates(keep='first')

happyusar=happy[['Country','Happiness Score']]
happyusar

data=pd.merge(Global,happyusar,on='Country',
                   how='inner')


#Asignamos country a los indices


matriz_variables=data[['Aritmetica','Algebra',
                        'Geomteria','Economia',
                        'Econometria']]

# Matriz de correlaciones
matriz_corr=np.corrcoef(matriz_notas,rowvar=False)


