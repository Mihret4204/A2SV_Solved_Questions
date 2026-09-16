class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        elif n<10000:
            return n-1000+1
        else:
            return 9000+(n-10000)+1
       