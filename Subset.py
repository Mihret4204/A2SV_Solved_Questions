#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        counter={}
        for i in a:
            counter[i]=counter.get(i,0)+1
        for j in b:
            if counter.get(j,0)>0:
                counter[j]-=1
            else:
                return False
        return True
        
    
    
    
    
