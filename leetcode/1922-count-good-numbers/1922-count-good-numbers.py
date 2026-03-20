class Solution:
    def countGoodNumbers(self, n: int) -> int:
        e=ceil(n/2)
        o=n//2
        ans=(pow(5,e,10**9 + 7)*pow(4,o,10**9 + 7))%(10**9+ 7)
        
        return ans