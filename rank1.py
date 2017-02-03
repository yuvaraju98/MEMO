#!/bin/python3

import sys
ans=[]
add=0

t = int(input().strip())
for a0 in range(0,t):
    num=input()
    num=int(num)
    for r in range(3,num):
        if r%3==0 and r%5!=0:
            print(r)
            
            add=add+r
            '''print(add)'''
        if r%5==0and r%3!=0 :
            add=add+r;
    ans.append(add)
    '''print(ans)'''
   
for m in range(t):
    print(ans[m])