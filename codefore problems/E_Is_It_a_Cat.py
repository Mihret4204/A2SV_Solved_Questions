t = int(input())

for _ in range(t):
    n=int(input())
    s=input().strip().lower()

    word=s[0]

    for i in range(1, n):
        if s[i] != s[i - 1]:
            word+= s[i]

    if word=="meow":
        print("YES")
    else:
        print("NO")