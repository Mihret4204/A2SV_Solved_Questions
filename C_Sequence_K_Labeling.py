from collections import defaultdict
n,k=map(int,input().split())
arr=list(map(int,input().split()))
s=defaultdict(list)
for i in range(n):
    s[arr[i]].append(i)
for c in s:
    if len(s[c])>k:
        print('NO')


