t = int(input())
arr = [-1]*1002
def dp():
    i = 1
    x = 1
    while i<1002:
        if x%3==0 or x%10==3:
            x+=1
            continue
        arr[i]=x
        i+=1
        x+=1

dp()

for _ in range(t):
    a = int(input())
    print(arr[a])
