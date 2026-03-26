class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.recursion(n,k)+1
    def recursion(self, n: int, k: int):
        if n==0:
            return 0
        return (self.recursion(n-1,k) + k)%n