#r=a[1]
    res.append(a[0])
    l=a[0]
    prev=a[1]-l
    for i in range(2,n):
        curr=a[i]-a[i-1]
        if curr*prev<0:
            res.append(a[i-1])
        prev=curr
    
    res.append(a[-1])
    print(len(res))
    print(*res)