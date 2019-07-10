https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem



n, k = [int(x) for x in input().split()]
clouds = list(map(int, input().strip().split()))
s=0
for i in range(0, n, k):
    s+=1 + 2 * clouds[i]
print(100-s)
