class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def ds(i):
            s = i
            total=0
            while s>0:
                total+=s%10
                s//=10
            pro=1
            while i>0:
                pro*=(i%10)
                i//=10
            return pro+total

            
            

        return n%ds(n)==0