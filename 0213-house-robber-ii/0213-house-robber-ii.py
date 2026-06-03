class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(arr_nums):
            memo = [-1] * len(arr_nums)

            def rec(i):
                if i == 0:
                    return arr_nums[0]
                if i == 1:
                    return max(arr_nums[0], arr_nums[1])

                if memo[i] != -1:
                    return memo[i]

                memo[i] = max(
                    rec(i - 2) + arr_nums[i],
                    rec(i - 1)
                )
                return memo[i]

            return rec(len(arr_nums) - 1)

        return max(
            solve(nums[:-1]),
            solve(nums[1:])
        )