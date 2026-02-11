class Solution:
    def isHappy(self, n: int) -> bool:
        while n>=10:
            sum=0
            while n>0:
                x=n%10
                sum+=x**2
                n//=10
            n=sum

        return n==1 or n==7