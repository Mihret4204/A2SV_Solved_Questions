t=int(input())
arr=list(map(int,input().split()))

total=0
for i in range(t+1):
    total+=i
print(total-sum(arr))