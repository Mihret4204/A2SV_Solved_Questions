n, s = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
curr = 0
left = 0
total=n*(n+1)//2
for right in range(n):
    curr += arr[right]
    while curr >= s and left <= right:
        curr -= arr[left]
        left += 1
    count += right - left + 1

print(total-count)