class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1:
            return n
        ans = i = 0
       
        while i<=n-k:
            for l in (k,k+1):
                if i+l<=n and s[i:i+l]== s[i:i+l][::-1]:
                    ans+=1
                    i+=l
                    break
            else:              
                i+=1
        return ans