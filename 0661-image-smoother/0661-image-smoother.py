class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows=len(img)
        cols=len(img[0])
        ans=[[0]*cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                total =0
                count=0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if 0<=i+dr<rows and 0<=j+dc<cols:
                            total+=img[i+dr][j+dc] 
                            count+=1
                ans[i][j]=total//count

                    
        return ans