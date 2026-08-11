for _ in range(int(input())):
    s = input()
    p = int(input())
    cnt = [0] * 27
    sm = 0
    for c in s:
        i = ord(c) - 96
        cnt[i] += 1
        sm += i
    
    for i in range(26, 0, -1):
        while cnt[i] > 0 and sm > p:
            cnt[i] -= 1
            sm -= i
    
    ans = ''
    for i in range(1, 27):
        ans += chr(96 + i) * cnt[i]
    print(ans)