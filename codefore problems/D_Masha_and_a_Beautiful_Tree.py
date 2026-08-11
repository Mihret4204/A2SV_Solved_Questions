t=int(input())

for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    ans=0
    def possible(l,r):
        
        mid=l+(r-l)//2

        min_l,max_l=possible(l,mid)
        min_r,max_r=possible(mid,r)

        if max_l<min_r:
            return min_l,max_r
        elif max_r<min_l:
            ans+=1
            return
    
    possible(0,n)
    print(ans)