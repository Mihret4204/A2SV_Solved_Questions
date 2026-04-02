class Solution:
    def isValid(self, s: str) -> bool:
        pairs={'(': ')', '{': '}', '[' : ']'}

        arr=[]

        for i in s:
            if i in pairs.keys():
                arr.append(i)
            elif i in pairs.values():
               
                if arr and pairs[arr[-1]]==i:
                    arr.pop()
                else:
                    return False 
        return arr==[]
