from collections import Counter

for _ in range(int(input())):
    s = input().strip()
    cnt = Counter(s)
    left = ''.join(c * cnt[c] for c in sorted(cnt))
    print(left + left[::-1])