class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        l=1
        for i in range(len(nums)-1):
            l*=nums[i]
            pre.append(l)
        r=1
        for i in range(len(nums)-1,-1,-1):
            pre[i]*=r
            r*=nums[i]
        return pre