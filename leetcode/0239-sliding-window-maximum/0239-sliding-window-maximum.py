class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        ans=[]

        for i,val in enumerate(nums):

            while q and q[-1]<val:
                q.pop()
            q.append(val)

            if k<=i and nums[i-k]==q[0]:
                q.popleft()
            if i+1>=k:
                ans.append(q[0])
        return ans