n = int(input())
for i in range(n):
    a = int(input())
    if a<3:
        print(0)
    elif a%2==0:
        print((a//2)-1)
    else:
        print(a//2)