class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        
        for i in range (left,right+1):
            con=True
            if i>0:
                j=i
                while j>0:
                    k=j%10
                    if  k==0 or i%k!=0:
                        con=False
                        break
                    j//=10

                if con:
                    ans.append(i)

        return ans
