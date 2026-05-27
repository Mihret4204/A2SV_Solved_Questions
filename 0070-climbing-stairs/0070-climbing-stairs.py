class Solution:
    
    def climbStairs(self, n: int) -> int:
        arr = [0]*46
        def rec(n):
            if n==1:  
                return 1
            elif n==2:  
                return 2
            elif arr[n]!=0:
                return arr[n]
            else :
                arr[n]=rec(n-1)+rec(n-2)
                return arr[n]

        return rec(n)

        