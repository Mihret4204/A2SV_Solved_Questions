k, i, t= map(int,input().split())

ans=k*(t*(t+1))//2 - i
if ans>0:
    print(ans)
else:
    print(0)