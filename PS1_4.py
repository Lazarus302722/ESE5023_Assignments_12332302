# -*- coding: utf-8 -*-
"""
Add or Double

The fastest way should be double, if the interger cannot be directed reached by doubling
then minus 1 to get the next step

@author: Alcorion
"""
import numpy as np
def Least_moves(x):
   step=0
   while x!=1 :
        if np.mod(x,2)==0:
            x=x/2
            step=step+1
        else:
            x=x-1
            step=step+1
   return step


#Realization of random number from 1 to 100  
l=input('input the number:')
l=int(l)
L=str(l)
Lm=Least_moves(l)
print('the least steps to',L,'is',Lm )

        
        