class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        _map={}
        _arr = sorted(set(arr))
        for i in range(len(_arr)):
            _map[_arr[i]] = i+1
        for i in range(len(arr)):
           
            arr[i]= _map[arr[i]]
        return arr