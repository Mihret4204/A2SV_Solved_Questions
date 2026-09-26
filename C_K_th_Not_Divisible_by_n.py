from math import ceil
t = int(input())
for _  in range(t):
    n,k = map(int,input().split())
    a = (k-1)//(n-1)
   
    print(a+k)
    