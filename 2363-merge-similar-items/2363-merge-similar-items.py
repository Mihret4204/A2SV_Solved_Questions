class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        _map = defaultdict(int)
        for v,w in items1:
            _map[v]+=w
        for v,w in items2:
            _map[v]+=w
        ans = []
        for k,v in _map.items():
            ans.append([k,v])
        ans.sort(key = lambda x: x[0] )
        
        return ans
