from collections import deque
t = int(input())

for _ in range(t):
    str= input()
    n,k = map(int,input().strip().split())

    graph = [[] for _ in range(n+1)]
    freq = [0]*(n+1)
    for _ in range(n-1):
        a,b = map(int,input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

        freq[a]+=1
        freq[b]+=1
    if n == 1:
        if k>0:
            print(0)
        else:
            print(1)
        continue

    q = deque()
    removed = [0]* (n+1)
    for i in range(1,n+1):
        if freq[i]<=1:
            q.append((i,1))

    rem =n
    while q:
        node, step = q.popleft()
        if step>k:
            break
        if removed[node]:
            continue
        removed[node]=1
        rem -=1
        for nei in graph[node]:
            if not removed[nei]:
                freq[nei]-=1
                if freq[nei]==1:
                    q.append((nei,step+1))

   
    print(rem)