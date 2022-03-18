# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:47:01 2021

@author: proje7
"""

import numpy as np
#0 ve 1lerden oluşan arrayler oluştur
x1 = np.zeros(5)
x2 = np.ones(5)
#7 ile 41
x3 = np.arange(7, 42, 2)

x4 = np.random.randint(1, 10, 16).reshape(4,4)

x5 = np.linspace(0.1, 1, 10)

x6= np.arange(25).reshape(5,5) # satırlardan 1. ve 2.index olanları, sütunlardan 3. ve 4. index olanları
x7 = x6[1:3,2:4]
print(x6)
print(x7)

#
x8 = np.arange(1,17).reshape(4,4)
x9 = x8[(x8 % 2 == 0)]
print(x8)
print(x9)
x10 = x9.reshape(2,4)
print(x10)

# x1 + x2 = 100 ve 5x1 + 10x2 = 700
A = np.array([[1, 1], [5, 10]])
B = np.array([100, 700])
x11 = np.linalg.solve(A, B)
print(x11)



