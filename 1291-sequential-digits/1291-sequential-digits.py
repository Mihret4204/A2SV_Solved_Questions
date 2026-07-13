class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        st = '123456789'
        start = len(str(low))
        end = len(str(high))
        ans = []

        for i in range(start,end+1):
            for j in range(10-i):
                num = int(st[j:j+i])
                if low<=num and num<=high:
                    ans.append(num)
        return ans