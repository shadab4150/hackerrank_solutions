"""""
https://www.hackerrank.com/challenges/30-bitwise-and/problem
""""
#python 3

#!/bin/python3

import math
import os
import random
import re
import sys

def shadab(n,k):
    arr1=[]
    for i in range(1,k):
        for j in range(i+1,2*k):
            c=i & j
            if c<k:
                arr1.append(c)
    return arr1

t=int(input())
arr=[]
for i in range(t):
    n,k=[int(x) for x in input().split()]
    print(max(shadab(n,k)))
    

#### Time complexity O(1)

test_cases = int(input().strip())
for i in range(test_cases):
    n, k = [int(x) for x in input().split()]
    result = (k - 1) if (((k - 1) | k) <= n) else (k - 2)
    print(result)
