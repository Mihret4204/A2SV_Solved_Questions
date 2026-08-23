class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        _map = {}
        n = len(nums)
        if k==n:
            return max(nums)
        for i in range(n):
            _map[nums[i]]=_map.get(nums[i],0)+1
        
        if k==1:
            ans = -1
            for i,val in _map.items():
                if val==1:
                    ans=max(ans,i)
            return ans

        
        if _map[nums[-1]]==1 and _map[nums[0]]!=1:
            return nums[-1]
        elif _map[nums[-1]]!=1 and _map[nums[0]]==1:
            return nums[0]
        elif _map[nums[-1]]==1 and _map[nums[0]]==1:
            return max(nums[-1],nums[0])
        return -1
        
        