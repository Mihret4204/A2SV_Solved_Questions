t = int(input())
for i in range(t):
    arr = list(map(int,input().split()))
    a = arr[0]
    arr.sort(reverse=True)
    
    print(arr.index(a))