s  = input()
i = 0
n=len(s)
ans=''
con = False
while i<n:
    
    if i<n-2 and s[i]=='W'and s[i+1]=='U' and s[i+2]=='B':
        if con:
            ans+=' '
        i+=3  
        con = False   
    else:
        con=True
        ans+=s[i]
        i+=1
print(ans)