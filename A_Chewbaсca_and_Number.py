s = input()
ans = 0
arr=[]
for i in range(len(s)):
    if i==0 and s[i]=='9':
        arr.append('9')
    elif s[i]>'4':
        arr.append(str(9-int(s[i])))
    else:
        arr.append(s[i])
print(''.join(arr))

