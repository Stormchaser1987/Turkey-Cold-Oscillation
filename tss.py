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
data = pd.read_csv("C:/Users/user/Desktop/TSSdata.txt")  # Verimizi okuyalım
x = data['Yil'] # Metrekareleri bir axis' e çekelim, panda nın özelliği.
y = data['Pressure']
z=sum(data['Pressure']/71)
print(data)
# Remove extra space in columns
print(x)
print(y)
print(z) # Ne oluşturduğumuza bakmak önemli.
plt.xlabel('Yil')
plt.ylabel('Pressure')
plt.title('Fransada Yıllara Göre 500 MB Basınç-Mart') # Ne oluşturduğumuza 2 boyutlu grafikte bakalım.
#Doğrumuzun denklemi y = m*a+b , Biz ise en uygun m ve b yi arıyoruz. m Eğim, b kesim noktası
regr = LinearRegression()
regr.fit(data[['Yil']], data[['Pressure']])


df = pd.read_csv("C:/Users/user/Desktop/TSSData2.txt")  # Verimizi okuyalım
a = df['Yil'] # Metrekareleri bir axis' e çekelim, panda nın özelliği.
b = df['Pressure']
c=sum(df['Pressure']/71)
print(df)
# Remove extra space in columns
print(a)
print(b)
print(c) # Ne oluşturduğumuza bakmak önemli.
plt.xlabel('')
plt.ylabel('')
plt.title('Türkiyede Yıllara Göre 500 MB Basınç-Nisan')

T=((y-z)-(b-c))/50
plt.title('Türkiye Soğuk Salınımı-Mayıs')
plt.scatter(x,T)
plt.plot(x,T)
pd.set_option('display.max_rows', 71)
print(T)

