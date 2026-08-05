class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        possible=set()

        for n in arr1:
            while n>0:
                possible.add(str(n))
                n//=10
        
        ans=0
        for n in arr2:
            num=n
            l=len(str(n))
            
            while num>0:
                s=str(num)
                if s in possible:
                    ans=max(ans,l)
                    break
                num//=10
                l-=1


        
        return ans
