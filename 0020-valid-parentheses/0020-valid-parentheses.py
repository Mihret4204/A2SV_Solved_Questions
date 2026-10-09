class Solution:
    def isValid(self, s: str) -> bool:
        pairs={'(': ')', '{': '}', '[' : ']'}

        arr = []

        for c in s:
            if c in pairs.keys():
                arr.append(c)
            else:
                if  arr and pairs[arr[-1]]==c:
                    arr.pop()
                else:
                    return False
        return arr==[]
        