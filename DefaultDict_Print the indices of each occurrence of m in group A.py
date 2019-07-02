https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

In this challenge, you will be given 2 integers, n and m.
There are n words, which might repeat, in word group A.
There are m words belonging to word group B.
For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A.
If it does not appear, print −1.




from collections import defaultdict
d = defaultdict(list)

x,y=[int(x) for x in input().split(' ')]
list1=[]
for i in range(x+y):
    if(i<x):
        d[input()].append(i+1)
    else:
        list1.append(str(input()))    
for i in list1:
    if i in d:
        print(" ".join(str(x) for x in d[str(i)]))
    else:
        print(-1)
