class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend//divisor>2147483647:
            return 2147483647
        if dividend//divisor<-2147483648:
            return -2147483647
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0): 
            return dividend//divisor  
        else:
            if dividend%divisor==0:
                return dividend//divisor
            return dividend//divisor+1