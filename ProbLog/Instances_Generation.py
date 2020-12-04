# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:49:32 2020

@author: cleiton
"""
import pandas as pd
df = pd.read_csv('chestcases100.csv',sep=';',dtype='string')
n, n_cols = df.shape

s=[]
f = open("chest_clinic_instances.pl", "w")
for i in range(n):
    for j in range(n_cols):
        s.append('evidence('+df.columns[j]+','+df.iloc[i][j]+').\n')
    if i!=n-1: s.append('---\n')
    
f.writelines(s)
f.close()

