class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        C={}
        ans=[0]*n
        for i in range (n):
            C[A[i]]=C.get(A[i],0)+1
            C[B[i]]=C.get(B[i],0)+1
            
            if A[i]==B[i]:
                ans[i]=ans[i-1]+1
            else:
                
                if C[A[i]]>1 and C[B[i]]>1:
                    ans[i]=ans[i-1]+2
                elif C[A[i]]>1 or C[B[i]]>1:
                    ans[i]=ans[i-1]+1
                else:
                    ans[i]=ans[i-1]

            
        
        return ans