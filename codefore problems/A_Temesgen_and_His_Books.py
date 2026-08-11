t=int(input())

for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    m=max(arr[:n-1])
    print(m+arr[-1])
    