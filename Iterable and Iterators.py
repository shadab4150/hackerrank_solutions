"""
https://www.hackerrank.com/challenges/iterables-and-iterators/problem
"""
#Python 3 Using loop

from itertools import combinations

n=int(input())
s=input().split()
k=int(input())

combinations_list=list(combinations(s,k))

result=list(filter(lambda x: 'a' in x ,combinations_list))

count=0

for i in combinations_list:
    if 'a' in i:
        count+=1

print(count/len(combinations_list))

#python 3 using filter

from itertools import combinations

n=int(input())
s=input().split()
k=int(input())

comb=list(combinations(s,k))

result=list(filter(lambda x: 'a' in x ,comb))

print(len(result)/len(comb))
