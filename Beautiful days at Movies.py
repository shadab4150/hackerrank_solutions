https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem



s,en,k=[int(x) for x in input().split()]
arr=[]
def beatifulDays(s,en,k):
    count=0
    for i in range(s,en+1):
        n=(str(i)[::-1])
        if abs(i-int(n))%k==0:
            arr.append(i)
            val+=1
    return count
print(beatifulDays(s,en,k))
        
    
