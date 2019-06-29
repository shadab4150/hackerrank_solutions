n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(' '))))
for i in range(len(arr)):
    for j in range(1):
        if abs(int(arr[i][j])-int(arr[i][j+2]))<abs(int(arr[i][j+2])-int(arr[i][j+1])):
            print("Cat A")
        elif abs(int(arr[i][j])-int(arr[i][j+2]))>abs(int(arr[i][j+2])-int(arr[i][j+1])):
            print("Cat B")
        else:
            print("Mouse C")
