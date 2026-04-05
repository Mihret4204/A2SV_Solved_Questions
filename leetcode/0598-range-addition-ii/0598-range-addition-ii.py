class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mr=m
        mc=n
        for i in range (len(ops)):
            mr=min(ops[i][0],mr)
            mc=min(ops[i][1],mc)
        return mr*mc
