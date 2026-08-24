
t = o = c = d = i = 0
n = int(input())
for j in range(n):
    a=input()
    if a == 'Tetrahedron':
        t+=1
    if a == 'Cube':
        c+=1
    if a == 'Octahedron':
        o+=1
    if a == 'Dodecahedron':
        d+=1
    if a == 'Icosahedron':
        i+=1
print(((t*4)+(c*6)+(o*8)+(d*12)+(i*20)))
