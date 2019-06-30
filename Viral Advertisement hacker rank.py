https://www.hackerrank.com/challenges/strange-advertising/problem

b=int(input())
day1=5
liked=0
share=0
for i in range(b):
    like=int(day1/2)
    share=like*3
    day1=share
    liked+=like       
print(liked)
