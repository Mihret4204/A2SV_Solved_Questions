class Solution:
    ans = []
    def __init__(self, nums: List[int]):
        self._map = defaultdict(list)
        for i, val in enumerate(nums):
            self._map[val].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self._map[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)