class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        i=len(nums)//3
        my_dic={}
        ans=[]
        for num in nums:
            my_dic[num]=my_dic.get(num,0)+1
        for idx,val in my_dic.items():
            if val>i:
                ans.append(idx)            
        return ans
        