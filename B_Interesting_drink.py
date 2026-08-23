t = int(input())
arr = list(map(int,input().split()))
arr.sort()
n = int(input())
for i in range(n):
    a = int(input())

    l, r = 0, t

    while l < r:
        mid = l + (r - l) // 2

        if arr[mid] <= a:
            l = mid + 1
        else:
            r = mid

    print(l)