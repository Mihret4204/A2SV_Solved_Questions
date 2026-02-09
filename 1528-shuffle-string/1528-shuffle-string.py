class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str=""
        store={}
        j=0
        for i in indices:
            store[i]=s[j]
            j+=1
           

        stores=dict(sorted(store.items()))
        for c in stores.values():
            str+=c
        return str

        