https://www.hackerrank.com/challenges/sherlock-and-squares/problem

"""
Counts the number of square integers (inclusive) between two given numbers.

"""
#!/usr/bin/env python

# For shortnumbers till 10^6

import math
n=int(input())
arr=[]
for k in range(n):
    i,j=[int(x) for x in input().split()]
    arr.append([i,j])
for k in range(len(arr)):
    count=0
    for t in range(arr[k][0],arr[k][1]+1):
        ar=math.sqrt(t)
        if (ar-math.floor(ar))==0:
            count+=1
    print(count)
 
 
 
# For any length number
 
# Time complexity O(2n)
 
 
import math
n=int(input())
arr=[]
for k in range(n):
    i,j=[int(x) for x in input().split()]
    arr.append([i,j])
for k in range(len(arr)):
    count = math.floor(math.sqrt(arr[k][1])) - math.floor(math.sqrt(arr[k][0] - 1))    
    print(count)

# Time complexity O(n)
    
import math
n=int(input())
for k in range(n):
    i,j=[int(x) for x in input().split()]
    count = math.floor(math.sqrt(j)) - math.floor(math.sqrt(i - 1))
    print(count)
