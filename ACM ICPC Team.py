"""
https://www.hackerrank.com/challenges/acm-icpc-team/problem

"""
"""
Short Problem Definition:
You are given a list of N people who are attending ACM-ICPC World Finals. 
Each of them are either well versed in a topic or they are not. 
Find out the maximum number of topics a 2-person team can know. 
And also find out how many teams can know that maximum number of topics.

"""

# TIme complexity O(n^3+n)

n,m=[int(x) for x in input().split()]
 
arr=[]

for i  in range(n):
    arr.append(str(input()))

arr2=[]

for i in range(0,n):
    
    for j in range(i+1,n):
        
        count=0
        man=0
        for k in arr[i]:
            
            t=arr[j][man]
            
            man+=1
            
            if k=='1' or t=='1':
                count+=1
        
        arr2.append(count)

print(max(arr2))

print(arr2.count(max(arr2))) 

# Time Complexity O(n^2)

n,m=[int(x) for x in input().split()]
 
arr=[]

for i  in range(n):
    arr.append(int(input(),2))
arr2=[]
for i in range(n):
    for j in range(i+1,n):
        num=arr[i] | arr[j]
        dat=bin(num)
        dat=dat[2:]
        count=dat.count('1')
        arr2.append(count)
max_topics=max(arr2)
print(max_topics)

print(arr2.count(max_topics))       

        
