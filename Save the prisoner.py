https://www.hackerrank.com/challenges/save-the-prisoner/problem



t=int(input())
for i in range(t):
    n,m,s=[int(x) for x in input().split()]
    place=(s-1+m)%n
    if place==0:
        place=n
    print(place)
    
