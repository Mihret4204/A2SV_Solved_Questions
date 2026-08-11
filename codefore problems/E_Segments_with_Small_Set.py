n, k = map(int, input().split())
arr = list(map(int, input().split()))

from collections import defaultdict

freq = defaultdict(int)
l = 0
ans = 0

for r in range(n):
    freq[arr[r]] += 1


    while len(freq) > k:
        freq[arr[l]] -= 1
        if freq[arr[l]] == 0:
            del freq[arr[l]]
        l += 1

    ans += (r - l + 1)


print(ans)
