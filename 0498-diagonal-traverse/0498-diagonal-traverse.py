class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        rows=len(mat)
        cols=len(mat[0])
        s=0
        ans=[]
       
        for d_sum in range(0,rows+cols-1):
            diagonal =[]
            r_start=max(0,d_sum-cols+1)
            r_end=min(d_sum,rows-1)

            for r in range (r_start,r_end+1):
                c=d_sum-r
                diagonal.append(mat[r][c])
            if d_sum%2==0:
                diagonal.reverse()
            ans.extend(diagonal)
                   
        return ans