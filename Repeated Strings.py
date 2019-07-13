https://www.hackerrank.com/challenges/repeated-string/problem

#python 3

s=input()
n=int(input())
no_a=s.count('a')
we=int(n/len(s))
if n%len(s)==0:
    print(no_a*we)
else:
    att=no_a*we
    for i in s[:n%len(s)]:
        if i=='a':
            att+=1
    print(att)
            
 
