t = int(input())
for _  in range(t):
    a = input()
    i=0
    ans = ''
    for i in range(0,len(a),2):
        ans+=a[i]
    print(ans+a[-1])