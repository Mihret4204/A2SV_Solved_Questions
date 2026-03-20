s=input()
dis=set()
for c in s:
    dis.add(c)
if (len(dis))%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
