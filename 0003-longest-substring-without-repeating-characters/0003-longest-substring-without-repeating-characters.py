class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans=0
        store=set()
        for r in range (len(s)):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            store.add(s[r])
            ans=max(ans,r-l+1)
        return ans
