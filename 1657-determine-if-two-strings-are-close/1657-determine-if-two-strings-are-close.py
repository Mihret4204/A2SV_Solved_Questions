class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1=Counter(word1)
        count2=Counter(word2)
        if len(word1)!=len(word2):
            return False
        if set(count1.keys())!=set(count2.keys()):
            return False
        freq1=sorted(count1.values())
        freq2=sorted(count2.values())
        print(freq1,freq2)
        if freq1==freq2:
            return True
        else:
            return False
        