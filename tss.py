# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:45:12 2018

@author: user
"""
import numpy as np
import datetime
import pandas as pd
import math
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("TSSdata.txt")  # Verimizi okuyalım
x = data['Yil'] # 
y = data['Pressure']
z=sum(data['Pressure']/71)
print(data)

print(x)
print(y)
print(z) 
plt.xlabel('Yil')
plt.ylabel('Pressure')
plt.title('Fransada Yıllara Göre 500 MB Basınç-Temmuz')
regr = LinearRegression()
regr.fit(data[['Yil']], data[['Pressure']])


df = pd.read_csv("C:/Users/user/Desktop/TSSData2.txt")  # Verimizi okuyalım
a = df['Yil']
b = df['Pressure']
c=sum(df['Pressure']/71) # TSS formülü
print(df)

print(a)
print(b)
print(c) 
plt.xlabel('')
plt.ylabel('')
plt.title('Türkiyede Yıllara Göre 500 MB Basınç-Temmuz')

T=((y-z)-(b-c))/50
plt.title('Türkiye Soğuk Salınımı-Temmuz')
plt.scatter(x,T) #Grafiğe dökelim.
plt.plot(x,T)
pd.set_option('display.max_rows', 71)
print(T) #Yazdıralım

