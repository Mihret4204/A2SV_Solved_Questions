class Solution:
    def minimumPushes(self, word: str) -> int:
        a = Counter(word)
        arr = []
        for k,val in a.items():
            arr.append(val)
        arr.sort(reverse = True)
       
        ans = 0
        for i in range(len(arr)):
            ans+=((i//8)+1)*arr[i]
        return ans