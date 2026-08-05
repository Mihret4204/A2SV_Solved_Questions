n = int(input())

for i in range(n):
    s = input()
    arr = s.split('+')
    print(int(arr[0])+int(arr[1]))