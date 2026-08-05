class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        #upper -> 26 and lower ->26
        #65-90 (upper) , 97 - 122(lower)

        upper = [False]*26
        lower = [False]*26

        for c in word:
            if c.islower():
                lower[ord(c)-ord('a')]=True
            else:
                upper[ord(c)-ord('A')]=True
        ans = 0 
        for i in range(26):
            if upper[i] and lower[i]:
                ans+=1
        return ans
