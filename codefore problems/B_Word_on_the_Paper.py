t = int(input())

def fun(arr):
    
    for i in range(8):
        for j in range(8):
            if arr[i][j]!='.':
                return [i,j]
                    
                

for _ in range(t):
    arr =[]
    ans=''
    for _ in range(8):
        s = input()
        arr.append(s)
    i,j = fun(arr)
    k =i
    while k<8 and arr[k][j]!='.' :
        ans+=arr[k][j]
        k+=1
    print(ans)