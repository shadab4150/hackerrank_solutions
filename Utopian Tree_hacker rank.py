https://www.hackerrank.com/challenges/utopian-tree/problem

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
k=max(arr)
l=[]
c=1
for i in range(1,k+1):
    if (i%2==0):
        c+=1
    else:
        c=c*2
    for j in range(len(arr)):
        if i==int(arr[j]):
            l.append(c)
        elif int(arr[j])==0:
            l.append(1)
zas=set(l)
man=sorted(zas)
shadab=dict(zip(sorted(arr),man))

for i in range(len(arr)):
    if int(arr[i]) in shadab:
        print(shadab[int(arr[i])])
