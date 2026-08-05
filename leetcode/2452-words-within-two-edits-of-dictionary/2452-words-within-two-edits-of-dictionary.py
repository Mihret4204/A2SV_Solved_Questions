class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans=[]
        for c in queries:
            for d in dictionary:
                a=0
                for i in range (len(c)):
                    if c[i]!=d[i]:
                        a +=1
                        if a>2:
                            break
                if a<3:
                    ans.append(c)
                    break
        return ans