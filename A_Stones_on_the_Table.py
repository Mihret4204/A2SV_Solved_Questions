n=int(input())
s=input()
l=0
for r in range(n-1):
    if s[r]==s[r+1]:
        l+=1
    
print(l)