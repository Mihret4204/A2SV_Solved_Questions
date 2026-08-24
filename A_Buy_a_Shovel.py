n,k = map(int,input().split())
ans = 1
for i in range(1,11):
    if (n*i)%10 == 0 or (n*i)%10 == k:
        ans = i
        break
print(ans)