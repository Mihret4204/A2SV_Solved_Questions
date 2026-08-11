t = int(input())
for _ in range(t):
    s = input()
    ans = set()
    
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        length = j - i
        
        if length % 2 == 1:
            ans.add(s[i])
        
        i = j
    
    print("".join(sorted(ans)))