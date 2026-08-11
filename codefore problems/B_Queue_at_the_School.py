n , t = map(int,input().split())
s = input()
arr = list(s)


 
for j in range(t):
    i=0
    while i<n-1:
            if arr[i]=='B' and arr[i]!=arr[i+1]:
                  arr[i],arr[i+1]=arr[i+1],arr[i]
                  i+=1
            i+=1
                

print(''.join(arr))

