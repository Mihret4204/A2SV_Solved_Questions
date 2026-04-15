class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mid=float('-inf')
        
        stack=[]

        for i in range (len(nums)-1,-1,-1):
            if mid>nums[i]:
                return True
            else:
                while stack and stack[-1]<nums[i]:
                    mid=stack.pop()
            stack.append(nums[i])

        return False
