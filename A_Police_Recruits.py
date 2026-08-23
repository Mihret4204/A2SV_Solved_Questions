t = int(input())
arr = list(map(int,input().split()))
ans = 0
pre = 0
for n in arr:
    if n == -1 and pre<1:
        ans+=1
    elif n == -1 and pre>0:
        pre-=1
    else:
        pre+=n
print(ans)