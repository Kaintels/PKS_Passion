# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 03:09:11 2019

@author: S. Han
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np #import package

lst = pd.read_csv('KakaoTalk_Longtxt_20190130_1202_50_393.txt', names=['pred', 'ans'])
lst = lst.sort_values(['pred'], ascending=True)
lst = lst.reset_index(drop=True) #data read


lst['pred'] = lst['pred'].str[7:10]
lst['ans'] = lst['ans'].str[7:10] #data processing
lstnp = np.array(lst, dtype=np.int) 
pred = lstnp[:,:1]
ans = lstnp[:,1:] #data type transform and processing

pred_mean = np.mean(pred)
ans_mean = np.mean(ans)
averg = np.ones(31) #count of data is 30
avergA = averg * pred_mean
avergB = averg * ans_mean
sss = (pred-avergA)*(ans-avergB)
sssS = sum(sss)
ppp = np.std(pred) * np.std(ans)
cor = sssS /(31 * ppp) #correlation

cor_print = cor[1] #only one array extract

plt.figure(figsize=(6,6), dpi = 100)
plt.scatter(pred,ans)
plt.xlim(120, 140)
plt.ylim(120, 140) #x and y lim

plt.title('CC : ' + str(round(cor_print, 3)))
plt.xlabel('pred')
plt.ylabel('ans')

x = [a for a in range(160)]
y = [b for b in range(160)] #make line
plt.plot(x,y, 'k') 
plt.show()
