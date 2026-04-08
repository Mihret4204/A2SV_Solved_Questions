class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=[]
        for i in range(len(matrix)):
            if matrix[i][-1]>=target:
               arr=matrix[i]
               break
        l=0
        r=len(arr)-1

        while l<=r:
            mid=l+(r-l)//2

            if arr[mid]==target:
                return True
            elif target > arr[mid]:
                l=mid+1
            else:
                r=mid-1
        return False