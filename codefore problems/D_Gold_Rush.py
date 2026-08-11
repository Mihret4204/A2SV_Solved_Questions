import sys
sys.setrecursionlimit(10**7)
t=int(input())

def main(n,m):
    if n==m:
        return True
    if n<m or n%3!=0:
        return False
    else:
        return main(n//3,m ) or main(2*n//3,m ) 
for _ in range(t):
    n,m=map(int,input().split())
    x=main(n,m)
    if x:
        print("YES")
    else:
        print("NO")   