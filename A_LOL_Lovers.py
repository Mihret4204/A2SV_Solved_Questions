from collections import Counter
n=int(input())
s=input()
ans=-1
con=False

c=Counter(s)
x={'L':0,'O':0}
r={'L':0,'O':0}

for i in range(n-1):    
    if s[i]=='L':
        x['L']=x['L']+1
    else :
        x['O']=x['O']+1
    r['L']=c['L']-x['L']
    r['O']=c['O']-x['O']
    #print(r,x)
    
    if x['L']!=r['L'] and x['O']!=r['O']:
        ans=i+1
        con=True
        break
if con==True:
    print(ans)
else:
    print(-1) 
        




