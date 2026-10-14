n, m = map(int, input().split())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

x = n + 1

while not is_prime(x):
    x += 1

if x == m:
    print("YES")
else:
    print("NO")