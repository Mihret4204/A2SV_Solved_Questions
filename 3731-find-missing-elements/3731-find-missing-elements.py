class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        n= nums[0]

        for i in range(len(nums)):
            while nums[i]!=n and n<nums[-1]:
                ans.append(n)
                n+=1
            n+=1

        return ans