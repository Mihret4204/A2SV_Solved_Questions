class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans=""
        for word in dictionary:
            j=0
            for i in range(len(s)):
                if j>=len(word):
                    break 
                if word[j]==s[i]:
                    j+=1
                    i+=1
                else:
                    i+=1
            if j==len(word) and len(ans)==len(word):
                ans=min(ans,word)
            elif j==len(word) and len(ans)<len(word):
                ans=word
            else:
                continue 
        return ans
    