s = input()
if len(s)==1:
    c = s[0]
    if c.isupper():
        print(c.lower())
    else:
        print(c.upper())
elif (s[0].islower() and s[1:].isupper()) or s.isupper():
    a = ''
    for c in s:
        if c.isupper():
            a+=c.lower()
        else:
            a+=c.upper()
    print(a)
else:
    print(s)