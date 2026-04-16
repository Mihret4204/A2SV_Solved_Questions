t=int(input())

for _ in range(t):
    a,b=map(int,input().split())
    if a%b==0:
        print(0)
    else:
        x=(a//b)+1
        print(x*b-a)