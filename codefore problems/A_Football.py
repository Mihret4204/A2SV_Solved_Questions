s = input()
a = 0
con = False
curr = s[0]
a = 1
for i in range(1,len(s)):
    
    if curr != s[i]:
        a = 1
        curr = s[i]
    else:
        a+= 1
        if a > 6:
            con = True
            break
if con:
    print("YES")
else:
    print("NO")
    