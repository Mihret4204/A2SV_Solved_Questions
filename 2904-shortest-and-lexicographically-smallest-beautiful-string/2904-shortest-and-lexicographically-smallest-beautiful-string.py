class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i = 0
        j  = 1
        n = len(s)
        ans = float('inf')
        p = s[:1].count('1')

        if k==1 and  '1' in s:
            return '1'

        
        while j<n:
            
            if s[j]=='1':
                p+=1
           
            if p==k :
                ans = min((int(s[i:j+1]),ans))
            while p>=k or s[i]=='0':
                if i>=j:
                    break
                if s[i]=='1':
                    p-=1
                i+=1
            j+=1
            

        if ans == float('inf'):
            return ''
        else:
            return str(ans)

            