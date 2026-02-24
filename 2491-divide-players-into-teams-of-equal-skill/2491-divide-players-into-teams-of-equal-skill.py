class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        ans=0
        if n%2!=0:
            return -1
        skill.sort()
        total=skill[-1]+skill[0]
        for i in range(n//2):
            if skill[i]+skill[n-i-1]!=total:
                return -1 
            ans+=skill[i]*skill[n-i-1] 
        return ans