t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    drops = 0
    for i in range(n):
        if a[i] > a[(i + 1) % n]:
            drops += 1

    if drops <= 1:
         print("Yes")
    else :
        print("No")