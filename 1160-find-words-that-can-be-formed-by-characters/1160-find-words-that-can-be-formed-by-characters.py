class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum=0
        main={} #main string container
        for c in chars:
            main[c]=main.get(c,0)+1
        for word in words:
            arr_word={} #string in our array
            is_good=True
            for a in word:
                arr_word[a]=arr_word.get(a,0)+1
            for char,count in arr_word.items():
                if main.get(char,0)<count:
                    is_good=False 
                    break 
            if is_good:
                sum += len(word)
        return sum 
                 
                
        
        