class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        _lower = {}
        _upper = {}
        ans = 0

        for i, c in enumerate(word):
            if c.islower():
                _lower[c]=i
            elif c.isupper() and c not in _upper:
                _upper[c]=i
    
        for c in _lower:
            letter=c.upper()
            if letter in _upper:
                if _upper[letter] > _lower[c]:
                    ans+=1
        
            
        return ans

            
                    

            
        
        return ans