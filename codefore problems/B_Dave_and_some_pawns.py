import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    enemy = list(input().strip())
    mine = list(input().strip())
    
    enemy = list(map(int, enemy))
    
    ans = 0
    
    for i in range(n):
        if mine[i] == '1':
            
            if i > 0 and enemy[i-1] == 1:
                ans += 1
                enemy[i-1] = 0
            
            elif enemy[i] == 0:
                ans += 1
            
           
            elif i < n-1 and enemy[i+1] == 1:
                ans += 1
                enemy[i+1] = 0
    
    print(ans)