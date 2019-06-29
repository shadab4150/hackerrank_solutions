b,k,m=[int(x) for x in input().split(' ')]
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
price=[]
new=[]
exp=[]
for i in range(k):
    for j in range(m):
        
        price.append(int(arr1[i])+int(arr2[j]))
for i in range(len(price)):
    if int(price[i])<=b:
        new.append(price[i])
    else:
        exp.append(price[i])
price1=sorted(new)
if b<int(min(price)):
    print(-1)
else:
    print(price1[-1])
