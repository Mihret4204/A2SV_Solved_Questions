from collections import defaultdict,deque
t=int(input())
_map=defaultdict(list)

arr=[0]*(t+1)
for _ in range(t-1):
    a,b=map(int,input().split())
    _map[a].append(b)
    _map[b].append(a)
    arr[a]+=1
    arr[b]+=1
q=deque()
ans=[]
e=0
x=False
for i in range(t):
    if x and arr[i]==1:
        e=i
    elif arr[i]==1:
        q.append(i)
        x=True
    
        
visited=set()

while q:
    
    node=q.popleft()
    ans.append(node)
    visited.add(node)
    if len(ans)==t:
        break
    for nei in _map[node]:
        
        if nei not in visited and e!=nei: 
            q.append(nei)
print(ans+[e])