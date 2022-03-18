# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:21:47 2021

@author: proje7
"""
import numpy as np

# Fancy Indexing
x1 = np.linspace(1, 21, 11) # [ 1.  3.  5.  7.  9. 11. 13. 15. 17. 19. 21.]
print(x1)
x2 = np.array([2, 4, 7]) # [2 4 7]
print(x2)

print(x1[x2]) # [ 5.  9. 15.]

x3 = np.arange(25).reshape(5,5)
print(x3)
x4 = np.array([1,2])
print(x4)
x5 = x3[x4,:] # x3 dizisini x4 dizisi yardımıyla değiştiriyoruz. x4 dizi [1 2] şeklindedir.
#Böylelikle x3 dizisinin değişiklik yapmak istediğimiz alanı satırdır burada ve başlangıç tarafındadır.
print(x5) # x3'ün 1. ve 2. index olan satırları x5 oldu artık
x6 = x3[:,x4]  # Burada ise x6 dizisinin sütunlarını alıyoruz
print(x6)  # x3' ün 1. ve 2. sütunu gösterecektir.
x6[0, 0] = 99
print(x6) # x6' nin 0.satır ve 0. sütunundaki eleman değişti
print(x3) # fancy indexin yaptığımız için yani bir diziyi başka bir dizi ile atadığımız, değiştirdiğimiz için
#x3 değişmedi

#%% Boolean Indexing

x7 = np.arange(10)
print(x7)

x8 = x7[(x7 % 2 == 0)]
print(x8)

x8[0] = 99
print(x8)
print(x7) #Boolean indexing yaptığımız için x7den türeyen dizinin aslı değişmedi yine.

x9 = np.linspace(1, 21, 11) 
print(x9) # [ 1.  3.  5.  7.  9. 11. 13. 15. 17. 19. 21.]
mask = (x9 % 3 == 0) #Maske bir nevi filtre oluşturduk
print(mask) #[False  True False False  True False False  True False False  True]
x9[mask] = 89 #x9' un bu mask koşulundaki True olan değerleri istediğimiz gibi değiştirdik
print(x9)

