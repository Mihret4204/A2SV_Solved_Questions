t = int(input())
for _ in range(t):
    s=input()
    s.lower()
    c = 'codeforces'
    ans = 0
    for i in range(10):
        if s[i]!=c[i]:
            ans+=1
    print(ans)