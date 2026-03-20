s=input()
vowels=["A", "O", "Y", "E", "U", "I","a", "o", "y", "e", "u", "i"]
ans=[]
for c in s:
    if c not in vowels:
        ans.append(c.lower())
print("."+".".join(ans))

