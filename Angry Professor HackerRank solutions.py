https://www.hackerrank.com/challenges/angry-professor/problem

b=int(input())
arr=[]
for i in range(2*b):
    arr.append(list(map(int,input().split())))
for i in range(2*b):
    if i%2==0:
        n=int(arr[i][0])
        k=int(arr[i][1])
        count=0
        for j in range(n):
            if int(arr[i+1][j])<=0:
                count+=1
        if count>=k:
            print("NO")
        else:
            print("YES")
                
    
