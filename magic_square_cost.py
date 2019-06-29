n=3
arr=[]
for i in range(3):
    arr.append(list(map(int,input().split(' '))))
    
matrix_list = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
               [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
               [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
               [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
               [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
               [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
               [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
               [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

mini=[]
for i in range(8):
    cost=0
    for j in range(3):
        for k in range(3):
            if arr[j][k]!=matrix_list[i][j][k]:
                cost+=abs(int(arr[j][k])-int(matrix_list[i][j][k]))
    mini.append(cost)
print(min(mini))
