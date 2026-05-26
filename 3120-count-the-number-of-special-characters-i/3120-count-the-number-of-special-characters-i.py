class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        _map=[0]*60
        for c in word:
            i=ord(c)-65
            _map[i]+=1
            
        ans=0
        for i in range(26):
            if _map[i]>0 and _map[i+32]>0:
                ans+=1
        return ans