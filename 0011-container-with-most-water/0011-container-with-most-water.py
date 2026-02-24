class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)-1
        ans=0
        width =n
        i=0
        j=n
        while i<j:
            width=j-i
            area=width*(min(height[i],height[j]))
            ans=max(ans,area)         
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
             
            
        return ans