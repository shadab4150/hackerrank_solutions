"""
https://www.hackerrank.com/challenges/picking-numbers/problem
"""
#Pyhton 3 Time complexity O(n+m)



from collections import Counter

n=int(input())
arr=list(map(int,input().split()))
cat=Counter(arr)
ele=list(set(arr))
ele=sorted(ele)
result=0
for i in range(len(ele)-1):
    if abs(ele[i]-ele[i+1])==1:
        man=cat[ele[i]]+cat[ele[i+1]]
        if man>result:
            result=man
for count in cat.values():
    if count>result:
        result=count
print(result)

        
     
