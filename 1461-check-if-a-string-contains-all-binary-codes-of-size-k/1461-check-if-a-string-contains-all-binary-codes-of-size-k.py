class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        store={}
        for i in range(len(s)-k+1):
            store[s[i:i+k]]=store.get((s[i:i+k]),0)
        
        if 2**k==len(store):
            return True
        else:
            return False
        