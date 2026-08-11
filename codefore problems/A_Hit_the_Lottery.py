n = int(input())
arr = [100, 20, 10, 5, 1]
ans = 0
val = 0
temp = n
for i in range(5):
    ans +=temp//arr[i]
    temp = temp%arr[i]
print(ans)