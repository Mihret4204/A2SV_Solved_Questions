class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total=0
        rem_map ={0:-1}
        for i in range(len(nums)):
            total+=nums[i]
            
            if total%k in rem_map:
                if i- rem_map[total%k]>1:
                    return True
            else:
                rem_map[total%k]=i
            
        return False