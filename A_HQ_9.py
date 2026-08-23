s = input()
con = False
for c in s:
    if c == 'H' or c == 'Q' or c == '9':
        con = True
        break
if con:
    print('YES')
else:
    print('NO')