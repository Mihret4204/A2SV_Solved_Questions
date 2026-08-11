n = int(input())
arr = []
for i in range(n):
    s = input()
    arr.append(s)
for i in range(n):
    s=arr[i]
    a = list(s[:3])
    b = list(s[-3:])
    s1, s2 = 0, 0
    for j in range(3):
        s1 += int(a[j])
        s2 += int(b[j])
    if s1==s2:
        print('YES')
    else:
        print('NO')