class Solution:
    def romanToInt(self, s: str) -> int:
        pairs={"I": 1,"V" : 5,"X" :10,"L" :50,"C":100,"D" :500,"M" :1000}
        ans=0
        for i in range(len(s)):
            current_num=pairs[s[i]]
            if (i+1)<len(s) :
                next_num=pairs[s[i+1]]
                if  next_num>current_num:
                    ans-=current_num
                else:
                    ans+=current_num                    
            else:
                ans+=current_num
        return ans
    