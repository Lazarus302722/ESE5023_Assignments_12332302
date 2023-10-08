# -*- coding: utf-8 -*-
"""
Pascal Triangle

@author: Alcorion
"""

def Pascal_triangle(k):
    if k==1:
        array=[1]
        return array
    elif k==2:
        array=[1,1]#initialize
        return array
    else:
        arraypre=Pascal_triangle(k-1)#find previous line
        array=[0 for x in range(0,k)]
        array[0]=1
        array[k-1]=1
        for i in range(k-2):
          array[i+1]=arraypre[i]+arraypre[i+1]
    return array    
        
Answer100=Pascal_triangle(100)
print(Answer100)
Answer200=Pascal_triangle(200)
print(Answer200)