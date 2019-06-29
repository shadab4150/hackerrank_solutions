from itertools import groupby
n=int(input())
arrt=list(map(int,input().split()))
groups = []
uniquekeys = []
p=sorted(arrt)
for k, g in groupby(p):
   groups.append(list(g))    
   uniquekeys.append(k)
pair=0
for i in range(len(uniquekeys)):
    if arrt.count(uniquekeys[i])>=2:
        pair+=int(arrt.count(uniquekeys[i])/2)
print(pair)
        
