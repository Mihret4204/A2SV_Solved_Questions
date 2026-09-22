t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    if b>a and b>c:
        print('PEAK')
    elif b>a and c>b:
        print('STAIR')
    else:
        print('NONE')