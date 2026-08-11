t=int(input())
 
for _ in range(t):
    store={}
    n,k=map(int,input().split())
    for i in range(k):
        b,c=map(int,input().split())
        store[b]=store.get(b,0)+c
    ans=[]
    for n in store.values():
        ans.append(n)
    ans.sort(reverse=True)
    print(sum(ans[:n]))
