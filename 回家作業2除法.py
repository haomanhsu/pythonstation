# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:22:07 2024

@author: Administrator
"""


import random

第一個數字 = (random.randint(1,100))

第二個數字 = (random.randint(1,100))




while 第一個數字 != 0 and 第二個數字 != 0:
    if 第一個數字 > 第二個數字:
        第一個數字 = 第一個數字 % 第一個數字
    elif 第二個數字 > 第一個數字:
        第二個數字 = 第二個數字 % 第一個數字
    else:
        break
if 第一個數字 == 0:
    print(第二個數字)
else:
    print(第一個數字)