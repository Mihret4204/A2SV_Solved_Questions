from math import sqrt
n = int(input())

for m in range(1,1000):
    x = n*m +1
    prime = True

    if x<2:
        prime= False
    else:
        num = int(sqrt(x))
        for i in range(2,num+1):
            if x % i == 0:
                prime = False
                break
    if not prime:
        print(m)
        break