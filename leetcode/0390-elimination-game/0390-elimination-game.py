class Solution:
    def lastRemaining(self, n: int) -> int:
        ans,step=1,1
        dir=True
        while n>1:
            if dir:
                ans+=step
            else:
                if n%2==1:
                    ans+=step
            step*=2
            n//=2
            dir=not dir
            
        return ans