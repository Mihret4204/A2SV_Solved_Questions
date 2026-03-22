n,t=map(int,input().split())
ans=[]
ans.append(t)
con=True
while t>n:
    if (t-1)%10==0:
        t=(t-1)//10
        ans.append(t)
    elif t%2==0:
        t=t//2
        ans.append(t)
    else:
        con=False
        break
ans.reverse()
if con and t==n:
    print("YES")
    print(len(ans))
    print(*ans)
else:
    print("NO")