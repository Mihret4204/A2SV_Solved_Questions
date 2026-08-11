n = int(input())
s = input().strip()

a = set(s.lower())

print("YES" if len(a) == 26 else "NO")