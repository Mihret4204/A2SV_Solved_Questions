class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        ans = ''
        for i in range (len(arr)-1,-1,-1):
            if i==0:
                ans=ans+arr[i]
            else:
                ans=ans+arr[i]+' '
        return ans