# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:23:57 2021

@author: proje7
"""

import time
import numpy as np

start_time = time.time()
A = np.arange(100000)
A ** 2
A_Time = time.time() - start_time

start_time2 = time.time()
B = range(100000)
[i ** 2 for i in B]
B_Time = time.time() - start_time2

print(B_Time/A_Time)

