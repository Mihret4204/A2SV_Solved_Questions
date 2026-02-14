class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split()
        if len(pattern)!=len(word):
            return False
        return len(set(zip(word,pattern)))==len(set(pattern))==len(set(word))