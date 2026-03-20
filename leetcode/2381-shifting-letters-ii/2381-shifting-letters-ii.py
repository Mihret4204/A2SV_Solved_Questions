class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        arr=[0]* n
        ans=""
        for i in range (len(shifts)):
           
            l,r,c=shifts[i][0],shifts[i][1],shifts[i][2]
            if  c==0:
                arr[l]-=1
            elif c==1:
                arr[l]+=1
            if  r+1<n and c==1:
                arr[r+1]-=1
            elif r+1<n and c==0:
                arr[r+1]+=1
        pre=0
        for i in range(n): 
            pre+=arr[i]
            print(pre)
            a=((ord(s[i])+pre-97)%26)+97
            ans+=chr(a)
        return ans
        