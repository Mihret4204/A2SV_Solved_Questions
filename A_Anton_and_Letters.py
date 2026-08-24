s = input().strip('{}').split(', ')

a = set()
for c in s:
    a.add(c)

if a=={''}:
    print(0)
else:
    print(len(a))