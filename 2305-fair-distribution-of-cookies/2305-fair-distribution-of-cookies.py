class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arr=[0]*k
        ans = float('inf')
        def backtrack(i,arr):
            nonlocal ans
            if i>=len(cookies):
                ans=min(ans,max(arr))
                return
            if max(arr)>ans:
                return

            for j in range (k):
                arr[j]+=cookies[i]
                backtrack(i+1,arr)
                arr[j]-=cookies[i]
        backtrack(0,arr)
        return ans

