https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays



#!/bin/python3

import math
import os
import random
import re
import sys

arr=[]
for i in range(6):
    arr.append(list(map(int,input().split(' '))))
max=0
for i in range(0,4):
    for j in range(0,4):
        sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if i==0 and j==0:
            max=sum
        elif sum>max:
            max=sum
print(max)
