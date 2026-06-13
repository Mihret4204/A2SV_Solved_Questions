class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        arr = []
        for word in words:
            a=0
            for l in word:
                v = ord(l)-97
                a=a + weights[v]
            b = 97 +  (25 - (a % 26)) 
            arr.append(chr(b))

        

        return ''.join(arr)
