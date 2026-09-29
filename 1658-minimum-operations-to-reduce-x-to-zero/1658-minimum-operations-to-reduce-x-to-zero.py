class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        tot = sum(nums)
        if x==tot:
            return n
        if x>tot:
            return -1
        
        l=0
        tar = tot-x
        res=-1
        s=0

        for r in range(n):
            s+=nums[r]
            while s>tar and l<=r:
                s-=nums[l]
                l+=1
            if s==tar:
                res=max(res,r-l+1)


        if res==-1:
            return -1
        return n-res
