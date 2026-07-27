class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dic = Counter(nums)
        ans = []
        i=len(nums)//3
        for idx,val in my_dic.items():
            if val>i:
                ans.append(idx)            
        return ans
        