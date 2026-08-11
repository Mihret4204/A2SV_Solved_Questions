t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    odd = []

    for c in s:
        if int(c) % 2 == 1:
            odd.append(c)
        if len(odd) == 2:
            break

    if len(odd) < 2:
        print(-1)
    else:
        print(odd[0] + odd[1])