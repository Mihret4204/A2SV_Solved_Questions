class Solution:
    def splitString(self, s: str) -> bool:
        
        def split(path,i):
            if i==len(s):
                for k in range(1,len(path)):
                    if  path[k] != path[k-1]-1:
                        return False
                return len(path)>=2
        
            for j in range(i,len(s)):
                val=int(s[i:j+1])
                path.append(val) 
                if split(path,j+1):
                    return True
                path.pop() 
            return False
        return split([],0)