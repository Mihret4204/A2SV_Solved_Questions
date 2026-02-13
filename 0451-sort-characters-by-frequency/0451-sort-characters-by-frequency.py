class Solution:
    def frequencySort(self, s: str) -> str:
        freq_dic={}
        ans=""
        for c in s:
            freq_dic[c]=freq_dic.get(c,0)+1
        sorted_dic=sorted(freq_dic.items(),key=lambda x :x[1], reverse=True)
        for char,count in sorted_dic:
                ans+=char*count
        return ans
                