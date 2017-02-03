t=input()
t=int(t)
for i in range(0,t):
    n=input()
    n=int(n)
    ist=[]
    ist.append(0)
    ist.append(1)
    ist.append(2)
    
    for j in range(3,n):
        
        ist.append(ist[j-1]+ist[j-2])
    '''print(ist)'''    
    sum=0
    '''for h in range(2,n):'''
    h=2
    while ist[h]<=n:    
        '''print(ist[h])'''
        if ist[h]%2==0:
            sum=sum+ist[h]
            '''print(ist[h])'''
        h+=1
            
    print(sum)  