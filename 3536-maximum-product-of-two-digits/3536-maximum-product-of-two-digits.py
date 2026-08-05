class Solution:
    def maxProduct(self, n: int) -> int:
        arr = list(map(int, str(n)))
        arr.sort()

        return arr[-1]*arr[-2]