n, B = map(int, input().split())
a = list(map(int, input().split()))

odd = 0
even = 0
costs = []

for i in range(n - 1):
    if a[i] % 2:
        odd += 1
    else:
        even += 1

    if odd == even:
        costs.append(abs(a[i] - a[i + 1]))

costs.sort()

ans = 0
spent = 0

for c in costs:
    if spent + c > B:
        break
    spent += c
    ans += 1

print(ans)