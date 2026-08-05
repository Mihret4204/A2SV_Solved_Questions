from collections import defaultdict
n,k = map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

groups = defaultdict(list)

for j,c in zip(a, b):
    groups[j].append(c)

extra= []

for job in groups:
    groups[job].sort()

    for x in groups[job][:-1]:
        extra.append(x)

miss=k-len(groups)

extra.sort()
print(sum(extra[:miss]))