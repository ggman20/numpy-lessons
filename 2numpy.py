# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:02:51 2021

@author: proje7
"""

import numpy as np

x = np.array([1, 2, 3], dtype = np.int)
print(x)
print(x.dtype)         

y = np.array([1, 2, 3], dtype = np.float)
print(y)
print(y.dtype)    

z = np.array([1, 2, 3], dtype = np.complex)
print(z)
print(z.dtype)  

a = np.array([1.3,2.6,3.8], dtype =np.int )   
print(a)

b= np.sqrt(np.array([-1, 4, 9]), dtype= np.complex)
print(b)
print(b.real)
print(b.imag)
# np.save('saveliarray', b)

np.load('saveliarray.npy')
print((b.real).dtype)
print((b.imag).dtype)