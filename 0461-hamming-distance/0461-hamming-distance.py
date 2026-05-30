class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit = x ^ y
        return bit.bit_count()