class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        mi = nums.index(min(nums))
        mx = nums.index(max(nums))
        l = min(mi, mx)
        r = max(mi, mx)        
        
        f = r+1
        b = n-l
        fb = (l+1) + (n-r)

        return min(f, b, fb)