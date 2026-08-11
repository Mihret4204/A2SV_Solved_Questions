s=input()
word=['h','e','l','l','o']
i=0
con=False
j=0
while i<5 and j<len(s):
    if i==4 and s[j]==word[i]:
        con=True
        break
    if s[j]==word[i]:
        i+=1
    j+=1
if con==True:
    print('YES')
else:
    print('NO')