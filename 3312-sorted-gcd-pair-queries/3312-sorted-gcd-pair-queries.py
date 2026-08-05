class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        
        mx = max(nums)
        freq = [0]*(mx+1)
       
        for num in nums:
            freq[num]+=1  

        for i in range(1,mx+1):
            for j in range(i*2,mx+1,i):
                freq[i]+=freq[j]
        
        for i in range(1,mx+1):
            freq[i] = freq[i]*(freq[i]-1)//2

        for i in range(mx,0,-1):
            for j in range(i*2,mx+1,i):
                freq[i]-=freq[j] 
        for i in range(1,mx+1):
            freq[i]+=freq[i-1]

        ans = []
        for i in queries:
            i+=1
            ans.append(bisect_left(freq,i))


        return ans