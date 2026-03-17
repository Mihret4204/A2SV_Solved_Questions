class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==1 or x==0:
            return x
        elif x==-1:
            if n%2==0:
                return 1
            else:
                return -1
        elif n==0:
            return 1
        elif n==1:
            return x
        elif n<0:
            
            return (1/((self.myPow(x,abs(n)))))
        elif n%2==0:
            return (self.myPow(x*x,n//2))
        else:
            return (self.myPow(x,n-1))*x
        