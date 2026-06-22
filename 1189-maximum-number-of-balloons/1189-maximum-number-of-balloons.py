class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        _b = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        _map = Counter(text)
       
        ans = []
        for b in _b.keys():
            if b not in _map.keys():
                return 0
           
            ans.append(_map[b]//_b[b])
        return min(ans)