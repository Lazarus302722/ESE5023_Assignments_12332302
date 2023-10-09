# -*- coding: utf-8 -*-
"""
Dynamic Programming

@author: Alcorion
"""
import numpy as np

def ten2three(x):
    po=0
    result=0
    while x>2:
        result=np.mod(x,3) * 10 ** po +result
        po=po+1
        x= x // 3
    result=10**po *x +result
    return result
        
def three2ten(x):
    po=0
    result=0
    while x > 0:
        result=result+np.mod(x,10) * 3 **po
        po=po+1
        x=x//10      
    return result


#def find_expression(x):
array=[0 for w in range(2*(3 ** 8)+1)]
p=0
for i in range(0,3**9):
    result=0
    de=ten2three(i+1)
    de=str(de)
    temp=1
    De= de.zfill(9)
    if int(De[0])==1:
        continue
   
    if int(De[0])==2:
        flag=-1
    else:
        flag=1
    for j in range(1,9):
        if int(De[j])==0:
            temp=temp *10 + j+1
        elif int(De[j])==1:    
            result=result+temp*flag
            flag=1
            temp=j+1
        else:
            result=result+temp*flag
            flag=-1
            temp=j+1
    array[p]=result
    p=p+1