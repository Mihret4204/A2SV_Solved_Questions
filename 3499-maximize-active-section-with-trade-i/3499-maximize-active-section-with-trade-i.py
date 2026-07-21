class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")
        t = "1" + s + "1"
        arr = []
        for ch in t:
            if not arr or arr[-1][0] != ch:
                arr.append([ch, 1])
            else:
                arr[-1][1] += 1
        best = 0
        for i in range(1, len(arr) - 1):
            if (arr[i][0] == "1" and arr[i - 1][0] == "0" and arr[i + 1][0] == "0"):
                best = max(best, arr[i - 1][1] + arr[i + 1][1])
        return ones + best