n,m,a=map(int,input().split())
r=a
c=a
while n<r:
    r+=a
while m<c:
    c+=a
print(max(r,c))