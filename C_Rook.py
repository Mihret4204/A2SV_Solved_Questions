r=int(input())
c=input()
a,b=c[0],c[1]
arr = ['a','b', 'c', 'd' , 'e', 'f','g', 'h']
for i in range(1,9):
    if i==int(b):
        continue
    s=a+str(i)
    print(s)
for i in range(1,9):
    if arr[i-1]==a:
        continue
    s=str(arr[i-1])+b
    print(s)