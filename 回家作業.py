# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:37:53 2024

@author: USER
"""

#四則運算

import random

第一個數字 = (random.randint(1,100))

第二個數字 = (random.randint(1,100))

問題 = input("請問你想選擇下列哪些選項 1 => + , 2 => - , 3 => *")


if 問題 == "1":
    print(f"你得到是{第一個數字+第二個數字}")
    
elif 問題 == "2":
    print(f"你得到的是{第一個數字-第二個數字}")
    
elif 問題 == "3":
    print(f"你得到的是{第一個數字*第二個數字}")
    
    
else:
    print("選項錯誤")