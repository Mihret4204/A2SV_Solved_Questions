class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lp = []
        mp = []
        m = []
        for n in nums:
            if n < pivot:
                lp.append(n)
            elif n == pivot:
                m.append(n)
            else:
                mp.append(n)
        return lp + m + mp