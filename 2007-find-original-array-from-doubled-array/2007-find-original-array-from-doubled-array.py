class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
             return []
        changed.sort()
        count = Counter(changed)
        res = []
        
        for x in changed:
            if count[x] == 0: 
                continue
            if count[x * 2] == 0: 
                return []
            res.append(x)
            count[x] -= 1
            if count[x * 2] <= 0: 
                return [] 
            count[x * 2] -= 1
        if len(res) == len(changed) // 2:
            return res  
        return []