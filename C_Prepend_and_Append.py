t =  int(input())
for _ in range(t):
    n = int(input())
    s = input()
    i,j = 0,n-1
    while i<j:
        if s[i]==s[j]:
            break
        i+=1
        j -=1
    print(j-i+1)