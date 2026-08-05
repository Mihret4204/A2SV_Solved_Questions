class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
        n = (l*(l+1))//2
        
        memo = [float(-inf)]*(n)
       
        def dp(i):
            
            if i==0:
                memo[i]=triangle[0][0]
           
            else:   
                idx = (i*(i+1))//2
                last = ((i)*(i-1))//2
                for j in range(len(triangle[i])):
                    
                    if j==0:
                        memo[idx+j] = triangle[i][j] + memo[last] 
                    elif j == len(triangle[i])-1:
                        memo[idx+j] = triangle[i][j] + memo[last+i-1]
                    else:
                        memo[idx+j] = triangle[i][j]+ min(memo[last+j],memo[last+j-1])
        for i in range(l):
            dp(i)
       
        ans =  min(memo[-l:])
        return ans