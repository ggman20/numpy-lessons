# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:21:59 2021

@author: proje7
"""

import numpy as np

x1 = np.zeros(4) #4x1' lik 0lardan oluşan matris
print(x1)
print(x1.dtype)
 
x2 = np.ones(4) #4x1' lik 1lerden oluşan matris
print(x2)
print(x2.dtype)

x3= np.zeros((2, 3, 4)) # 3 boyutlu bir matris. 2 tane 3 satırı ve 4 sütun olan matris
print(x3)

x4 = np.ones((4,5)) #2 boyutlu bir matris. 4 satırı ve 5 sütunu olan matris
print(x4)

x5 = np.full((2,3), 10) #2x3' lük 10lardan oluşan matris
print(x5) 

x6 = 10 * np.ones((2,3))
print(x6)

x7 = 10 + np.zeros((2,3))
print(x7)

# x5 = x6 = x7 'dir.

x8 = np.empty((2,3)) #2x3lük normalde bir matris.rastgele sayılar print eder.
print(x8)

x8.fill(3) #x8 adındaki boş nd arrayin içini 3 ile doldurur.
print(x8)

x9 = np.eye(6) #6x6'lık bir birim matris oluşturur.
print(x9)

x10 = np.eye(6, k=1) #6x6' lık bir matristir. 1. indexten itibaren diagonal 1ler oluşur.
print(x10)

x11 = np.eye(6, k= -2) #6x6' lık bir matristir. -2. indexten itibaren diagonal 1ler oluşur.
print(x11)

x12= np.identity(5) #5x5'lik bir birim matristir. np.eye ile aynıdır.
print(x12)

x13 = np.diag([4,7,11,8])
print(x13)
