n=int(input())
s=input()
sea_level=0
VAL=0
for x in range(len(s)):
    if s[x]=='D':
        sea_level=sea_level-1
    else:
        sea_level=sea_level+1
    if sea_level==0 and s[x]=='U':
        VAL+=1
print(VAL)
