class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def back(start,path):
            ans.append(path)
            for i in range(start,len(nums)):
                back(i+1,path+[nums[i]])
            

            
        back(0,[])
        return ans
