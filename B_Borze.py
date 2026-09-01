s = input()
arr = ['.','.-','--']
i=0
n=len(s)
ans = ''
while i<n: 
    if s[i]=='.':
        ans+='0'
    elif s[i]=='-' and i<n:

        if s[i+1]=='-':
            ans+='2'
        else:
            ans+='1'
        i+=1
    i+=1
print(ans)