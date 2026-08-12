class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        n = len(nums)
        _map = {}
        i = 0
        j = 1
        ans = 1
        _map[nums[0]]=_map.get(nums[0],0)+1
        while j<n:
            _map[nums[j]]=_map.get(nums[j],0)+1
            
            if _map[nums[j]]>k:
                while i<j and _map[nums[j]]>k:
                    _map[nums[i]]=_map.get(nums[i],0)-1
                    i+=1
            j+=1   
            ans = max(ans,j-i)
            
        
        return ans