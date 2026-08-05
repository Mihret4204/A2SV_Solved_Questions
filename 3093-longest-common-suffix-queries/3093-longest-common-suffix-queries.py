class TrieNode:
    def __init__(self, value=""):
        self.index = float('inf')               
        self.wordLen = float('inf')        
        self.children = {}              
        self.is_end = False             


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index = 0):
        node = self.root
        length = len(word)

        if length < node.wordLen:
            node.wordLen = length
            node.index = index

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if length < node.wordLen:
                node.wordLen = length
                node.index = index

        node.is_end = True

    
    def find_max_suffix(self, word) -> int:
        node = self.root
        for ch in word[::-1]:
            if ch not in node.children:
                break
            node = node.children[ch]

        return node.index

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        n = len(wordsQuery)
        ans = [0] * n
        trie = Trie()

        for idx, word in enumerate(wordsContainer):
            rev = word[::-1]
            trie.insert(rev, idx)
        
        for i in range(n):
            ans[i] = trie.find_max_suffix(wordsQuery[i])
        
        return ans