n=int(input())
p=int(input())
if p==1 or p==n:
    print(0)
elif n%2==1:
    if p==n or p==n-1:
        t=0
    
elif n%2==0:
    
    
    if p>int(n/2):
        #print("b")
        t=int(n/2)-int(p/2)
    else:
        #print("a")
        t=int(p/2)
    print(t)

if n%2==1 and p>1 and p<n:
    
    
    if p>int(n/2):
        #print("d")
        m=int(n/2)-int(p/2)
    else:
        m=int(p/2)
        #print("c")
    print(m)
