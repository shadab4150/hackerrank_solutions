https://www.hackerrank.com/challenges/array-left-rotation/problem



x,y=[int(x) for x in input().split(' ')]
arr=list(map(int,input().split(' ')))
def shift(arr,y):
    return arr[y:]+arr[:y]
k=shift(arr,y)
print(" ".join(str(x) for x in k))
