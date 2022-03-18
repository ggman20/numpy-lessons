# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:46:52 2021

@author: proje7
"""
import numpy as np
x1 = np.random.randint(1, 10, size = 8)
x2 = np.random.randint(1, 10, size = 8)
x3 = np.add(x1,x2) # x3 = x4. İki şekilde de yapılabilir
x4 = x1 + x2
print(x1)
print(x2) 
print(x3) 
print(x4)
x5 = np.subtract(x1, x2) # x5 = x6
x6 = x1 - x2
print(x5)
print(x6)
x7 = np.multiply(x1, x2) # x7 = x8
x8 = x1 * x2
print(x7)
print(x8)
x9 = np.divide(x1, x2) # x9 = x10
x10 = x1 / x2
print(x9)
print(x10)
x11 = np.sqrt(x1) # x1 dizisi elemanlarının karekökünü alıp array olarak döndürür
x12 = np.power(x1, 3) # x1 dizisi elemanlarının küpünü alıp array olarak döndürür
x13 = np.exp(x1) # x1 dizisi elemanlarını e üzeri yani logaritma alıp array döndürür
print(x11)
print(x12)
print(x13)
x14 = np.random.randint(1, 10, size = (9,)).reshape(3,3)
print(x14)
x15 = x14.sum(axis = 0) #sütunları toplayarak 1x3lük matris yaptı
x16 = x14.sum(axis = 1) #satırları toplayarak 1x3lük matris yaptı
print(x15)
print(x16)
x17 = x14.min()
x18 = x14.max()
print(x17)
print(x18)