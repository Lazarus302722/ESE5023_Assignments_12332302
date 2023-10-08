# -*- coding: utf-8 -*-
"""
Multiplication of Matrix
@author: Alcorion
"""

#2.1 create matrix M1,M2
import numpy as np

M1=np.random.randint(0,51,(5,10))

M2=np.random.randint(0,51,(10,5))

#2.2 multiply realization
def Matrix_multip(M3,M4):
   #examine process
   (c1,c4)=M3.shape
   (c2,c3)=M4.shape
   if c2 != c4:
      print('error')#examine the illegal conditions
   else:
      (a,c3)=M3.shape
      (c4,b)=M4.shape
      M=np.zeros((a,b))
      for i in range(0,a):
        for j in range(0,b):
         for k in range(0,c1):
             M[i,j] = M[i,j]+M3[i,k] * M4[k,j]     
        #  M[i,j]=M1[i,:] * M2[:,j]
      print(M)
      
Matrix_multip(M1, M2)
