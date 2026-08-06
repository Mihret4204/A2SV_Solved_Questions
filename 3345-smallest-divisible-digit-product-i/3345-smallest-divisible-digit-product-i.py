class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+t):
            j = 1
            num = i
            while num>0:
                j*=(num%10)
                num//=10 
            if j%t==0:
                return i
            
