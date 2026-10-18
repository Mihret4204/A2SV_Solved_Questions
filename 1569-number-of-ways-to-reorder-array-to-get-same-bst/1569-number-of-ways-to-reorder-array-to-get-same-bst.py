class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod=10**9 + 7
        n = len(nums)
        b = [-1] * (n + 2)  
        for t, x in enumerate(nums):
            b[x] = t

        s = 1
        stack =  [0]  
        for v in range(1, n + 2):
            while b[stack[-1]] > b[v]: 
                stack.pop()
                s = s * (v - stack[-1] - 1) % mod 
            stack.append(v)

        a = 1
        for k in range(2, n + 1):
            a = a * k % mod
        return (a * pow(s, -1, mod) - 1) % mod