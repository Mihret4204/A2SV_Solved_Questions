class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        m =  10**9 + 7
        @cache
        def dp(i,cf1,cf2):
                                        
            if i==n:
                if cf1!=0 and cf2!=0 and cf1==cf2:
                    return 1
                else:
                    return 0
            return dp(i+1,cf1,cf2)+dp(i+1,cf1,gcd(cf2,nums[i]))+dp(i+1,gcd(nums[i],cf1),cf2)
            
            
        

        
        return (dp(0,0,0))%(10**9 + 7)