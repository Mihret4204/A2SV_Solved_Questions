class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        k=len(p)
        mapping=Counter(s[:k])
        mapp=Counter(p)
        if mapp==mapping:
                ans.append(0)
        for i in range(k,len(s)):
            mapping[s[i-k]]=mapping.get(s[i-k],0)-1
            mapping[s[i]]=mapping.get(s[i],0)+1
            if mapping[s[i]]==0:
                del mapping[i]
            if mapping[s[i-k]]==0:
                del mapping[s[i-k]]
            if mapp==mapping:
                ans.append(i-k+1)
            
        return ans
