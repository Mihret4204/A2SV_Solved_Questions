arr = list(map(int,input().split()))
arr.sort()
m = arr[1]
print(abs(arr[0]-m)+abs(arr[-1]-m))