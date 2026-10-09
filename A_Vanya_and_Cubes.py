n = int(input())
ans = 1
temp = 1
while n>=temp:
    ans+=1
    temp+=(ans*(ans+1))//2  
    
print(ans-1)