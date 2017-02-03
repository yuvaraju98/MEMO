test=input()
flag=[]
flag = [0]*1000
ans=[]
import itertools
from itertools import combinations
test=int(test)
for i in range(0,test):
    numberofshares=input()
    numberofshares=int(numberofshares)
    shares=[]
    for j in range(0,numberofshares):
        shares.append(input())
    addon=[]
    '''print(shares)'''
    for q in range(1,len(shares)+1):
        for subse in itertools.combinations(shares,q):
            
            add=0
            a=0
            while a!=len(subse):
                b=int(subse[a])
                add=add+b
                a+=1
            addon.append(add)
    '''print("addon set -",addon)'''
    numnewsh=input()
    numnewsh=int(numnewsh)
    numofantq=[]
    c=[]
    
    for l in range(0,numnewsh):
        numofantq.append(input())
    for z in range(0,numnewsh):
            
        c.append(input())
        
   
        
    for L in range(1, len(numofantq)+1):
        for subset in itertools.combinations(numofantq,L):
            '''print(subset,"length-",len(subset))'''
            ll=0
            '''while len(numofantq):
               print("is",len(subset) ,"is equal to",numofantq[ll] )
                '''
            for ll in range(0,len(numofantq)):
                
                req=int(len(subset))
                '''print("c",c[ll],ll,numofantq[ll],req)'''
                beq=int(numofantq[ll])
                
                if req==beq:
                    '''print(c[ll],"enterwdd")'''
                    sharp=int(c[ll])
                    uff=int(flag[ll])
                    if sharp in addon:
                        
                        '''print(c[ll],"Yes")'''
                        if uff is 0:
                            y="Yes"
                            ans.insert(ll,y)
                            flag[ll]=1
                        
                            
                        
                        ''''c.remove(c[ll])
                        numofantq.remove(numofantq[ll])'''
                    else:
                        if uff is 0:
                            flag[ll]=1
                            n="No"
                            ans.insert(ll,n)
                        '''print("No")'''
                        ''''c.remove(c[ll])
                        numofantq.remove(numofantq[ll])'''
                ll=int(ll)
                '''if ll>(beq):
                    ll-=1
                else:
                    break'''
            
    for d in range(0,len(ans)):
        print(ans[d])
    
    