https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

#!/bin/python3

n=int(input())
arr=list(map(int,input().split()))

def JumpOnClouds(arr):
    count=0
    i=0
    while i<n-1:
        if i<n-2 and arr[i+2]==0:
            i=i+2
            count+=1
        else:
            i=i+1
            count+=1
    return count

print(JumpOnClouds(arr))
