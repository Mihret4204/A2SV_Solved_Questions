class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        pre = 0 
        ans=[0]*(len(pref))
        ans[0] =  pref[0]
        for i in range(1,len(pref)):
            ans[i]=pref[i-1]^pref[i]
            
        return ans