class Solution:
    def findComplement(self, num: int) -> int:
        bit = 0
        com = num

        while com :
            bit = (bit<<1) ^ 1
            com >>=1
        return bit ^ num