class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def rec(n1):
            val=0   
            for j in range (1, len(n1)-1):
                
                if n1[j]> n1[j-1] and n1[j]> n1[j+1]:
                    val+=1
                elif  n1[j] < n1[j-1] and n1[j] < n1[j+1]:
                    val+=1
            return val
            
        ans = 0
        for i in range(num1,num2+1):
            if len(str(i))<3:
                continue
            m =  rec(str(i))
            ans+=m
                
                

        return ans