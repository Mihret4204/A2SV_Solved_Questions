import sys

def solve():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        
        a.sort()
        
        ok = True
        for i in range(1, n):
            if a[i] - a[i-1] > 1:
                ok = False
                break
        
        print("YES" if ok else "NO")

if __name__ == "__main__":
    solve()
