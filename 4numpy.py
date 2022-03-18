# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:07:52 2021

@author: proje7
"""

import numpy as np

x1 = np.arange(4,9) #[4 5 6 7 8]
print(x1) 

x2 = np.arange(2, 20, 3) #[2  5  8 11 14 17]
print(x2)

x3 = np.linspace(1, 9, 3) #[1. 5. 9.]
print(x3)

x4 = np.arange(20) #1x20lik matris
x5 = np.reshape(x4, (4,5)) #x4 matrisini 4x5lik matris haline getirdik.
print(x5)

x6 = np.random.random((2,3)) #2x3lük 0 ile 1 arasında rastgele matris üretir.
print(x6)

x7 = np.random.randint(5,15,size = (3,2)) # 5 ile 15 arasında 3x2lik matris oluşturur.
print(x7)