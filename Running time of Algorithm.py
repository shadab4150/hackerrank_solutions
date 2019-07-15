"""""

https://www.hackerrank.com/challenges/runningtime/problem

"""""

# Python 3

# Counting no of swaps it takes to sort an array accordingto insertion sort

# Using for and if loop

n=int(input())
arr=list(map(int,input().split()))

def InsertionSort(alist):
    No_of_Swaps=0
    for i in range(1, len(alist)):
        for j in range(i-1,-1,-1):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                No_of_Swaps+=1
            else:
                break 
        
        
    return No_of_Swaps

print(InsertionSort(arr))


# Using for and while

n=int(input())
arr=list(map(int,input().split()))

def InsertionSort(alist):
    No_of_Swaps=0
    for i in range(1, len(alist)):
        j=i-1
        while alist[j]>alist[j+1] and j>=0:
            alist[j],alist[j+1]=alist[j+1],alist[j]
            j-=1
            No_of_Swaps+=1
        
        
    return No_of_Swaps

print(InsertionSort(arr))

# Time Complexity O(n^2)


