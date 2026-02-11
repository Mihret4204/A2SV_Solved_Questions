class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store=defaultdict(list)
        for stri in strs:
            sorted_word="".join(sorted(stri))
            store[sorted_word].append(stri)
        return list(store.values())

        