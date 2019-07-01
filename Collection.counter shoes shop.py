https://www.hackerrank.com/challenges/collections-counter/problem
Task

Raghu is a shoe shop owner. His shop has X number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are N number of customers who are willing to pay (X) amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

#code

from collections import Counter
n=int(input())
arr=list(map(int,input().split(' ')))
m=int(input())
arr2=[]
for i in range(m):
    arr2.append(list(map(int,input().split(' '))))
c=Counter(arr)
cost=[]
for i in range(len(arr2)):
    for j in range(1):
        if arr2[i][j] in c:
            if int(c[int(arr2[i][j])])>0:
                c[int(arr2[i][j])]+=-1
                cost.append(int(arr2[i][j+1]))
print(sum(cost))
