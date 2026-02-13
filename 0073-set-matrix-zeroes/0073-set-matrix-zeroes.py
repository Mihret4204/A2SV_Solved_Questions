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
        for m in range(row):
                if m in rowz:
                    for n in range(col):
                        matrix[m][n]=0
        for x in range(col):
                if x in colz:
                    for y in range(row):
                        matrix[y][x]=0

        print(matrix)