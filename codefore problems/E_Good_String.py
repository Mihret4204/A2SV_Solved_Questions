t=int(input())
s=input()

ans=[]
i=0
while i<t:
    j=i+1
    while j<t and s[j]==s[i]:
        j+=1
    if j<t:
        ans.append(s[i])
        ans.append(s[j])
    i=j+1
    
    

print(t-len(ans))
print("".join(ans))

