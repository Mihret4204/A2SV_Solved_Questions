class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count=Counter(nums)
        i=0
        for _ in range(count[0]):
            nums[i]=0
            i+=1
        for _ in range(count[1]):
            nums[i]=1
            i+=1
        for _ in range(count[2]):
            nums[i]=2
            i+=1