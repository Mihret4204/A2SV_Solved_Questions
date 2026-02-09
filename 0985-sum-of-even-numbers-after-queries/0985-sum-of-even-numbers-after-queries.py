class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        sums = sum(x for x in nums if x % 2 == 0)
        n=len(queries)
        for i in range(n):
            if nums[queries[i][1]]%2==0:
                sums-=nums[queries[i][1]]
            nums[queries[i][1]]=nums[queries[i][1]]+queries[i][0]
            
            
            if nums[queries[i][1]]%2==0:
                sums+=nums[queries[i][1]]
            ans.append(sums)
        return ans

        