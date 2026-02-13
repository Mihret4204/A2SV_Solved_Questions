class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colz=set()
        rowz=set()
        print(matrix)
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    colz.add(j) 
                    rowz.add(i)             
        for i in rowz:
            for j in range(col):
                matrix[i][j] = 0
        for j in colz:
            for i in range(row):
                matrix[i][j] = 0

        print(matrix)