from collections import defaultdict
t = int(input())

for _ in range(t):
    n,m = map(int, input().split())

    graph = defaultdict(list)
    un_map = defaultdict(list)
    for i in range(m):
        arr = list(map(int,input().split()))
        if arr[0]==1:
            graph[arr[1]].append(arr[2])
        if arr[0]==0:
            un_map[arr[1]].append(arr[2])