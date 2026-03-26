class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        seen=defaultdict(int)
        seen[0]=1
        ans=0
        for n in nums:
            prefix+=n
            r=prefix%k 
           
            if seen[r]>0:
                ans=ans+seen[r]
            seen[r]=seen.get(r,0)+1
        
        return ans