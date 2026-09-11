class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()
        for a,b,c in permutations(digits,3):
            if a!=0 and c%2==0:
                ans.add((a,b,c))
        return len(ans)