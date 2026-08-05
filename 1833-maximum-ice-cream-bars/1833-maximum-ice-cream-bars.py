class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        _min = _max = max(costs)
        freq = [0] * (_max + 1)
        for x in costs:
            freq[x] += 1
            _min = min(_min, x)
        ans = 0
        for x, f in enumerate(freq[_min:], start=_min):
            if f == 0:
                continue
            buy = min(coins // x, f)
            if buy == 0:
                break
            ans += buy
            coins -= buy * x
        return ans