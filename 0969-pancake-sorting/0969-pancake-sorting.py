class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr),1,-1):
            maxi=max(arr[:i])
            k=arr.index(maxi)
            if k!=0:
                arr[:k+1]=arr[:k+1][::-1]
                ans.append(k+1)                
            arr[:i]=arr[:i][::-1]
            ans.append(i)           
        return ans


            

        