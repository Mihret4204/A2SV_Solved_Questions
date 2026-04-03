class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]

        arr=path.split('/')
       
        for i in arr:
            if i== '' or i=='/':
                continue 
            if '.' in i :
                if i=='.':
                    continue 
                if i=='..' :
                    if stack:
                        stack.pop()
                    else:
                        continue 
                else:
                    stack.append(i)
            else:
                stack.append(i) 

        return ('/'+'/'.join(stack))

        
                