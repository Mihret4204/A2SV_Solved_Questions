class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [-1]*(38)
        arr[0] = 0
        arr[1] = arr[2] = 1
        def trib(n):
            nonlocal arr
            if arr[n] != -1:
                return arr[n]
            arr[n] = (trib(n-1)+ trib(n-2)+ trib(n-3))
            return arr[n]
        return trib(n)