import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    w = input().strip()

    target = sum(ord(c) for c in w)
    cur = sum(ord(c) for c in s[:m])

    found = (cur == target)

    for i in range(m, n):
        cur += ord(s[i])
        cur -= ord(s[i-m])
        if cur == target:
            found = True
            break

    print("YES" if found else "NO")