class Solution:
    def mirrorDistance(self, n: int) -> int:
        a=str(n)
        a=a[::-1]
        a=int(a)
        return abs(a-n)