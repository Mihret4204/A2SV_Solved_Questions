from collections import Counter

n = int(input())
arr = list(map(int,input().split()))
freq = [[],[],[]]

for i in range(n):
    
    if arr[i]==1:
        freq[0].append(i)
    elif arr[i]==2:
        freq[1].append(i)
    elif arr[i]==3:
        freq[2].append(i)

a = freq[0]
b = freq[1]
c = freq[2]
ans = min(len(a),len(b),len(c))
print(ans)
for i in range(ans):
    print(a.pop()+1,b.pop()+1,c.pop()+1)
