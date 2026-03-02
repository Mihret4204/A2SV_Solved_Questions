class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        diff=[]
        for i in range(len(nums)-1):
            l=sum(nums[:i+1])
            r=sum(nums[i+1:])
            diff.append(r-l)
        count=0
        
        for x in diff:
            if x%2==0:
                count+=1
        return count