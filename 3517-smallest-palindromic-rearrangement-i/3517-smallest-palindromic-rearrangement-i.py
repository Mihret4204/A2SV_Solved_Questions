class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ans=""
        cs=Counter(s)
        css={key: cs[key] for key in sorted(cs)}
        odd = ""
        for i in css.keys():
            ans+=i*(css[i]//2)
            if (css[i]%2)!=0:
                odd += i
        rev=ans[::-1]
       
        return ans+odd+rev


        