n = int(input())
ans = 1

s = input()
for i in range(1,n):
    a = input()
    if s[-1]==a[0]:
        ans+=1
    s=a
print(ans)