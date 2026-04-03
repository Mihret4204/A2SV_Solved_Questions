class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr=[0]*(len(nums)+1)
        for s,l in requests:
            arr[s]+=1
            arr[l+1]-=1

        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]        
        arr.sort(reverse=True)
        nums.sort(reverse=True)
        print(arr,nums)

        ans=[]
        
        for i in range(len(nums)):
            ans.append(arr[i]*nums[i])
        res=sum(ans)
        return res % (10**9 + 7)