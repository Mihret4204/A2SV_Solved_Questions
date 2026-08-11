class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        arr = [float('-inf')]*n
        arr.append(0)

        
        for i in range(n-1,-1,-1):
            total = 0
            for j in range(i,min(n,i+3)):
                total+=stoneValue[j]
                arr[i]=max(arr[i],total-arr[j+1])
    

        
        if arr[0]>0:
            return "Alice"
        if arr[0]<0:
            return "Bob"
        else:
            return "Tie"