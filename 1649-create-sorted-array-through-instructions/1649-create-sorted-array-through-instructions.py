class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ans=0
        arr=SortedList()

        for n in  instructions:
            ans+=min(arr.bisect_left(n),len(arr)-arr.bisect_right(n))
            ans=ans%(10**9 + 7)
            arr.add(n)



        
        return ans