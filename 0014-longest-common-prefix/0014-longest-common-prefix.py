class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not any(strs):
            return ""
        prefix=strs[0]
        n=len(strs)
        l=len(prefix)
        for i in range(n): 
            if len(prefix)==0:
                return "" 
            while not strs[i].startswith(prefix):
                prefix=prefix[:-1]
        return prefix



        

        