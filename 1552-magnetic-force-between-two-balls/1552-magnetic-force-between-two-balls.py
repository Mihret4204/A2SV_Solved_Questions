class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def possible(d):
            k = 1
            start = position[0]
            for p in position[1:]:
                if p-start>=d:
                    k+=1
                    start=p
                    if m==k:
                        return True
            return False

        l = 1
        r = position[-1]
        ans = 1
        while l <= r:
            mid = l + (r - l) // 2
            print(mid)
            if possible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
