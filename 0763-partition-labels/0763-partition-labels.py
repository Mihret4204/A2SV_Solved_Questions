class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        ans=[]
        i=0
        j=1
        m=0
        while i<n:
            x=s[i]
            y=s[j:]
            if i==j:
                ans.append(j-m)
                m=j            
                j+=1    
            elif x in y:
                j+=1
                continue 
            elif x not in y:
                i+=1
       
        ans.append(n-m)   
        return ans
        
        