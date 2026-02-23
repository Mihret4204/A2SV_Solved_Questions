class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            total=numbers[right]+numbers[left]
            if total==target:
                break 
            elif total<target:
                left+=1
            else:
                right-=1
        return [left+1,right+1 ]