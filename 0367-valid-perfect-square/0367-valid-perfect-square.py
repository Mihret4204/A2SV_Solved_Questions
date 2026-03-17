class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<0:
            return False
        elif num==1 or num==0:
            return True
        i=2
        ans=1
        while i<=num//i:
            if i*i==num:
                return True
            i+=1
        return False
            
