# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:08:00 2021

@author: proje7
"""

import numpy as np

x1 = np.array([0,2,5,7,31,21])
x2 = np.array([1,8,7,21,88])

x3 = np.intersect1d(x1, x2) #kesişim kümesini buluruz.
print(x3) #[ 7 21]
x4 = np.setdiff1d(x1, x2) #x1' de olup x2' de olmayan elemanları gösterir.
print(x4) # [0 2 5 31]
x5 = np.union1d(x1, x2) #x1 ile x2'nin birleşim kümesini gösterir,kesişim elemanlarını bir kez gösterir.
print(x5) # [0 1 2 5 7 8 21 31 88]
x6 = np.in1d(x1,x2) #x1' in elemanlarına bakar.True False döndürür.
#Mesela x1in ilk elemanı 0 x2de var mı yok."False" döndürür.
#x1in 4.elemanı x2de var.Onu da "True" döndürür.
print(x6) # [False False False True False True] şeklinde yazdırır
x7 = ([0,1,2,5,8,2,5,31,21,80,55,21])
x8 = np.unique(x7) # x7 disinin benzersiz elemanlarını gösterir.Aynı elemanlar varsa 1 kez gösterir.
print(x8) # [ 0  1  2  5  8 21 31 55 80]
#%%Sıralama İşlemi
#sort
x9 = np.random.randint(1, 10, size = 8)
print(x9) # [9 1 8 7 9 8 4 2] 
x10 = np.sort(x9) #Burada fonksiyon olarak sort ediyoruz.
print(x9) # x9 tabi ki değişmedi
print(x10) #[1 2 4 7 8 8 9 9]
x9.sort() #metot olarak sort edince x9 da değişir.
print(x9) # x9 değişti çünkü metot olarak sort ettik artık x9u.
#2 BOYUTLU SORT ETME
x11 = np.random.randint(1, 10, size = (5,5))
print(x11)
x12 = np.sort(x11, axis = 0) #satırlara göre sıralar
x13 = np.sort(x11, axis = 1) #sütunlara göre sıralar
print(x12)
print(x13)
