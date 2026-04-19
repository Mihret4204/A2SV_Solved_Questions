class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rev=nums[::-1]
        ans=[]
        arr=[]
        for n in rev:
            i=bisect.bisect_left(arr,n)
            ans.append(i)
            bisect.insort(arr,n)
       
        
        return ans[::-1]