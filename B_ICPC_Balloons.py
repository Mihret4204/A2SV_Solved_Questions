t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
   
    c = set(s)
    
    print(len(s)+len(c))