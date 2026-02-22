class Solution:
    def binaryGap(self, n: int) -> int:
        s=str(bin(n)) 
        store={} 
        prev=-1 
        ans=0
        for i in range(len(s)):

            if s[i]=="1" and prev!=-1:
                ans=max(i-prev,ans)
                prev=i
            if s[i]=="1" and prev==-1:
                prev=i
        return ans              
        