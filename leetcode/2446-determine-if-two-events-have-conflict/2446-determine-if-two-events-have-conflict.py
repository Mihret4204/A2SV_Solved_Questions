class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1 , end1 = event1
        start2 , end2 = event2
        #if start1 or end1 enter b/n start2 and end2  or vise versa 
        if end1 >= start2 >= start1  or end1 >= end2 >= start1:
            return True
        if end2 >= start1 >= start2  or end2 >= end1 >= start2:
            return True
        return False