class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def solve(start1, dur1, start2, dur2):
            fin1 = float('inf')
            for i in range(len(start1)):
                fin1 = min(fin1,start1[i] + dur1[i])
            fin2 =  float('inf')
            for i in range (len(start2)):
                fini = max(start2[i],fin1)+ dur2[i]
                fin2=min(fin2,fini)
            return fin2
        
        a = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        b = solve(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(a,b)