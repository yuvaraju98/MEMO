
c=1
a=2
def dev():
    global a,c
    if c<1001 and a<1001:
        print(c)
        print(a)
        c+=2
        a+=2
        dev()
    
dev()   