class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        path=[]
        def comb(path, i):
            if len(path)==k:
                ans.append(path[:])
                return
            for j in range(i,n+1):
                path.append(j)
                comb(path,j+1)
                path.pop()
            return 

        comb([],1)
        return ans
