https://www.hackerrank.com/challenges/itertools-permutations/problem



from itertools import permutations
x,y=[str(x) for x in input().split(' ')]
k=sorted(list(permutations(x,int(y))))
for i in range(len(k)):
    print("".join(str(x) for x in k[i]))
