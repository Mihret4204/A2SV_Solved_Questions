class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ss="".join(sorted(s))
        st="".join(sorted(t))
        if ss==st:
            return True
        return False
        