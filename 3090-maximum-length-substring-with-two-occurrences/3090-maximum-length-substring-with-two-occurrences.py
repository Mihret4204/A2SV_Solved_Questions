class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 1
        _map = {}
        _map[s[i]] = 1
        ans = 0
        while j<n:
            _map[s[j]]=_map.get(s[j],0)+1
            if _map[s[j]] >2:
                while _map[s[j]]>2:
                    _map[s[i]]=_map.get(s[i],0)-1
                    i+=1
            ans = max(ans,j-i+1)
            j+=1
        return ans
