#prblem https://www.hackerrank.com/challenges/migratory-birds/problem
import math
import os
import random
import re
import sys


n=int(input())
arr=list(map(int,input().split(" ")))
def most_frequent(arr): 
    return max(set(arr), key = arr.count) 
print(most_frequent(arr))
