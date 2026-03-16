class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        if maxDoubles==0:
            return target-1
        if target ==1:
            return 0
        if target %2==0 and maxDoubles>0:
            count+=1
            maxDoubles-=1
            return self.minMoves(target//2,maxDoubles)+count
        else:
            count+=1
            return self.minMoves(target-1,maxDoubles) +count
        