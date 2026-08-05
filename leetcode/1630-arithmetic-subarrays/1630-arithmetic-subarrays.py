class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for j in range (len(l)):
            con = True
            left =l[j]
            right = r[j]
            arr = sorted(nums[left:right +1])
            for i in range (1,len(arr)-1):
            
                if arr[i]-arr[i-1] !=  arr[i+1]-arr[i]:
                    con = False
                    break 
            if con :
                ans.append(True)
            else:
                ans.append(False)
        return ans
