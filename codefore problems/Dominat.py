from collections import Counter
n=int(input().strip())
for i in range(n):
    str=""
    x=int(input().strip())
    s=input().strip()
    if "aa" in s:
        print(2)
    elif "aba" in s or "aca" in s:
        print(3)
    elif "acba" in s or "abca" in s:
        print(4)
    elif "abbacca" in s or "accabba" in s :
        print(7)
    else:
        print(-1)