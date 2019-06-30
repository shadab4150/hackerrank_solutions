https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


arr=list(map(int,input().split()))
s=input()
arr2=[]
letters='abcdefghijklmnopqrstuvwxyz'
for i in range(len(s)):
    arr2.append(arr[letters.index(s[i])])
print(int(max(arr2))*len(s))
