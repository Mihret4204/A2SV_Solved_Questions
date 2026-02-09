class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        ans=[]
        result=[]
        for i,num in enumerate(nums):
            store[num]=store.get(num,0)+1
        sorted_store=sorted(store.items(), key= lambda x: x[1] ,reverse=True)
        for m in range(k):
            result.append(sorted_store[m][0])
        return result
        