# -*- coding: utf-8 -*-
"""
Feel like the flowchart is a simplified sorting process


@author: Alcorion
"""

def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,',',b,',',c,sep='')#sep regulate output
        else:
            if a>c:
                print(a,',',c,',',b,sep='')
            else:
                print(c,',',a,',',b,sep='')
    else:
        if c>b:
            print(c,',',b,',',a,sep='')
        else:
            print()
            
a=input('a=')
b=input('b=')
c=input('c=')
Print_values(a,b,c)

            
