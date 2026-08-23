n, k, l, c, d, p, nl, np = map(int, input().split())

drink = k * l
lime = c * d
salt = p // np
dr = drink // nl

ans = min(dr, lime, salt)

print(ans // n)

