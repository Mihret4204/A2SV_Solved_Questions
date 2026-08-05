class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        visited = set()

        for c  in s:
            freq[c]-=1
            if c in visited: continue

            while stack and stack[-1]>c and freq[stack[-1]]:
                top= stack.pop()
                visited.remove(top)
                
            stack.append(c)
            visited.add(c)
        return "".join(stack)