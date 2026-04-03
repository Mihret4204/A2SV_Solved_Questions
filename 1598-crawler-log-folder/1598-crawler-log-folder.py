class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]

        for i in logs:
            print(stack)
            if  i == "../":
                if stack:
                    stack.pop()
                else:
                    continue 
            elif i=="./":
                continue 
            else:
                stack.append(i)
        return len(stack)
