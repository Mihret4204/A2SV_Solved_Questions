from collections import Counter
t = int(input())
for _  in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    cnt =Counter(arr)
   
    if len(cnt)>2 :
        print('NO')
    elif len(cnt)==2:
        if abs(cnt[arr[0]] - cnt[arr[-1]] ) <2:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
        
