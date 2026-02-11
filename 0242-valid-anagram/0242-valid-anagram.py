class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dic={}
        t_dic={}
        for x in s:
            s_dic[x]=s_dic.get(x,0)+1    
        for y in t:
            t_dic[y]=t_dic.get(y,0)+1   
        return s_dic==t_dic
        