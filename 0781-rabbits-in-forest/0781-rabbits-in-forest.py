class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans=0
        a=Counter(answers)     
        for k,val in a.items():  
            ans+=(val+k)//(k+1) *(k+1)         
        return ans
        