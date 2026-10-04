class Solution:
    def checkValidString(self, s: str) -> bool:
        mi = mx = 0

        for c in s:
            if c == '(':
                mi+=1
                mx+=1
            elif c==')':
                mi-=1
                mx-=1
            elif c == '*':
                mi-=1
                mx+=1
            if mx<0:
                return False
            if mi<0:
                mi=0
        return mi==0
