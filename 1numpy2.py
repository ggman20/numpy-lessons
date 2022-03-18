# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:48:22 2021

@author: proje7
"""

import numpy as np

y = np.array([[1,2,3], [4,5,6]])

print(y)
print(type(y))
print(y.shape)
print(y.size)
print(y.ndim)
print(y.nbytes)
print(y.dtype)

#y.shape herbir eksendeki eleman sayısını tuple olarak gösterir. (2, 3) 2 satır ve 3 sütun
#y.size toplam kaç eleman var? 6
#y.ndim kaç boyutlu olduğunu gösterir. 2
#y.nbytes elemanları kaç byte yer kaplar. 24
#y.dtype elemanların veri tipi. int32