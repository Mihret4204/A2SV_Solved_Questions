class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land =  len(landStartTime)
        wat = len(waterStartTime)
        ans = float('inf')

        for i in range (land):
            for j in range (wat):
                if waterStartTime[j] > landStartTime[i]:
                    m = max(waterStartTime[j] , (landStartTime[i] + landDuration[i] ) )
                    val = m + waterDuration[j]
                   
                else:
                    m = max (landStartTime[i],(waterDuration[j] + waterStartTime[j] ))
                    val = m + landDuration[i]  
                    
                ans = min(ans,val)
        return ans
