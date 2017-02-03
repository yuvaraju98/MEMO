import re
n =int(input(""))
m = input("")
d = dict()
for line in m:
    if line.startswith('G'):
        ls1 = re.findall('[0-9]+',line)
        for i in ls1:
            d[i] = d.get(i, 0)*4
            print(d.get(i,0))
    elif line.startswith('M'):
        ls2 = re.findall('[0-9]+',line)
        for j in ls2:
            d[j] = d.get(j, 0)*3
    
    ls = list()
    for a,b in d.items():
        ls.append((b,a))
        ls.sort(reverse=True)
        print(a,b)
        print(ls)
        if (ls[b][a] == '19' or ls[b][a] == '21'):
            print("Date")
        else:
            print("No Date")