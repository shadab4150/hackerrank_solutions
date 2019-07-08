https://www.hackerrank.com/challenges/word-order/problem


# Using Counter

from collections import Counter
n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
c=Counter(arr)
new=[]
order=[]
for i in arr:
    if i in c.keys():
        if i in new:
            dat="Do nothig"
        else:
            new.append(i)
            order.append(c[i])
print(len(c.keys()))
print(" ".join(str(x) for x in order))

# Using OrderedDict

import collections
n = int(input())
d = collections.OrderedDict()
for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(len(d))
print(" ".join(str(x) for x in list(d.values())))
