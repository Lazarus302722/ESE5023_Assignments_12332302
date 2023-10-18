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


def Find_expression(x):
 array=[0 for w in range(3 ** 8)]
 p=0
 for i in range(0,3**8):
    result=0
    de=ten2three(i)
    de=str(de)
    temp=1
    flag=1
    De= de.zfill(8)
    for j in range(8):
        if int(De[j])==2:
            temp=temp *10 + j+2
        elif int(De[j])==0:    
            result=result+temp*flag
            flag=1
            temp=j+2
        else:
            result=result+temp*flag
            flag=-1
            temp=j+2
    result=result +temp *flag
    array[p]=result
    p=p+1
 count=0  
 for k in range(6561):
    string=''
    if array[k]==x:
        count=count+1
        pro=str(ten2three(k)).zfill(8)
        num='123456789'
        for p in range(8):
            if int(pro[p])==0 and p!=0:
                mark='+'
            elif int(pro[p])==1:
                mark='-'
            else:
                mark=''
            string=string+num[p]
            string=string+mark
           
        string=string+'9='
        string=string+str(x)
        print(string)
 return count
            
#Total Solutions
Total_solutions=[0 for x in range(100)]
for idx in range(100):
    Total_solutions[idx]=Find_expression((idx+1))


import matplotlib.pyplot as plt
Xarr=np.arange(1,101)
plt.bar(Xarr,Total_solutions,color='b')
plt.show()
