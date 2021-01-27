#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:23:09 2021

@author: fxc
"""


import random
import string
import math
import numpy as np
import pandas as pd

list_nbr_tirage = list()

for _ in range(100000):
    
    billes = list(string.ascii_uppercase)[0:4]
    check = list(string.ascii_uppercase)[0:4]
    tirage = list()
    
    
    while len(check) != 0 :
        
        new_bille = random.choice(billes)
        
        if new_bille in check :
            check.remove(new_bille)
        
        tirage.append(new_bille)
    
    list_nbr_tirage.append(len(tirage))

df_nbr_tirage = pd.DataFrame(list_nbr_tirage)
df_nbr_tirage.plot.density()
mean = df_nbr_tirage.mean()
maxi = df_nbr_tirage.max()
mini = df_nbr_tirage.min()
