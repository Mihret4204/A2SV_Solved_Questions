class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        _map={}
        for word in words:
            _map[word]=_map.get(word,0)+1

        ans = sorted(_map.keys() ,key= lambda w : (-_map[w], w))
        return ans[:k]
