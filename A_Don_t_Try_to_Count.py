t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    s = input()
    st = input()
    ans = -1
    for i in range(6):
       
        if st in s:
            ans = i
            break
        s+=s
        
    print(ans)
        