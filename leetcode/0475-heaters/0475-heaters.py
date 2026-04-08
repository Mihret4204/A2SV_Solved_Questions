class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        def possible(radius):
            i,j=0,0

            while i<len(houses) and j<len(heaters):
                if abs(houses[i]-heaters[j])<=radius:
                    i+=1
                else:
                    j+=1
            return i==len(houses)


        l=0
        r=max(heaters[-1],houses[-1])
        while l<r:
            mid=l+(r-l)//2
            if possible(mid):
               r=mid
            else:
               l=mid+1
        return l
