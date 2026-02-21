n=int(input())
qns=list(map(int,input().split()))
qns.sort()
days=0
for i in range(n):
    if qns[i]>days:
        days+=1
        
print(days)
