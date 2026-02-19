class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ans=""
        cs=Counter(s)
        css={key: cs[key] for key in sorted(cs)}
        for i in css.keys():
            ans+=i*(css[i]//2)
        rev=ans[::-1]
        for val,i in css.items():
            if i%2!=0:
                ans+=val
            
        ans+=rev
        return ans


        