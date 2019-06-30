x,y=[int(x) for x in input().split(' ')] #y=dan height jump
arr=list(map(int,input().split(' ')))
hur_max=int(max(arr))
if y>=hur_max:
    print(0)
else:
    print(hur_max-y)
