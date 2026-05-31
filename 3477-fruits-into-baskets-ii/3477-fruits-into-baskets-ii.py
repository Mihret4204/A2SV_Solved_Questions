class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n =  len(fruits)
        ans=0
        for i in range(n):
            con = True
            for j in range(n):
                if baskets[j] >= fruits[i]:
                    baskets[j]=0
                    con = False
                    break
            if con:
                ans+=1
        return ans
