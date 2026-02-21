class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
       
        ans=0
        n=len(citations)
        for i in range(n):
            count=n-i
            if citations[i]>=count:
                return count                
        return ans
        