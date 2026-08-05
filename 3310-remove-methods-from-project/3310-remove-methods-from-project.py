class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        _map = defaultdict(list)
        in_degree = [0] * n
        for i,j in invocations:
            _map[i].append(j)
            in_degree[j]+=1
        
        que = [k]
        s = set([k])
        
        while que:
           
            i = que.pop()
            
            for j in _map[i]:
                if j not in s:
                    s.add(j)
                    que.append(j)

        res=[]            
        for i in range(n):
            if i in s:
                continue
            for nei in _map[i]:
                if nei in s:
                    ans = [m for m in range(n)] 
                    return ans
            res.append(i)
        return res
            
