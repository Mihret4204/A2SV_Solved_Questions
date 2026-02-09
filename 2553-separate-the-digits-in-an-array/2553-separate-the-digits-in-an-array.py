class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        numbers=[]
        for i in nums:
            c=str(i)
            for d in c: 
                numbers.append(int(d))
        return numbers