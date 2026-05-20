class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        _map={}
        for num in nums:
            _map[num]=_map.get(num,0)+1
        ans=[0,0]
        for i,val in _map.items():
            ans[0]+=val//2
            ans[1]+=val%2
        return ans