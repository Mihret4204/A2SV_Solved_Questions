class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        l=0
        r=x
        ans=0

        while l<=r:
            mid=l+ (r-l)//2

            if (mid*mid)>x:
                r=mid-1
            else:
                ans=mid
                l=mid+1
        return ans