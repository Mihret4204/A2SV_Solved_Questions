a=int(input())
b=int(input())
c=int(input())

ans = a + b + c
ans = max(ans, (a + b) * c)
ans = max(ans, a * (b + c))
ans = max(ans, a * b * c)

print(ans) 