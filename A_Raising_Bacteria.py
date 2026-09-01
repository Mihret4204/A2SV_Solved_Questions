
n = int(input())

ans = 0


b = bin(n)
for c in b:
    if c =='1':
        ans+=1
print(ans)