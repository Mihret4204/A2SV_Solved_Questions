class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        _map = defaultdict()
        for n in nums:
            _map[n]=_map.get(n,0)+1
        ans=0
        for i in _map.keys():
            if _map[i]==2:
                ans ^=i
        return ans