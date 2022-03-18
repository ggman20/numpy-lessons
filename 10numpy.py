# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:57:10 2021

@author: proje7
"""

import numpy as np

x1 = np.random.randint(1, 10 ,size = (8,))
print(x1)
x2 = x1.mean() #Aritmatik ortalaması
x3 = np.median(x1) #median değerini verir
x4 = x1.std() # standart sapmasını verir
print(x2)
print(x3)
print(x4)
#%% 2 BOYUTLU İÇİN;
x5 = np.random.randint(1, 10, size= (4,3))
print(x5)
x6 = x5.mean(axis = 0) #axis = 0 sütun için, axis = 1 satır için
x7 = x5.mean(axis = 1)
print(x6)
print(x7)
x8 = np.median(x5, axis = 0)
x9 = np.median(x5, axis = 1)
x10 = x5.std(axis = 0)
x11 = x5.std(axis = 1)