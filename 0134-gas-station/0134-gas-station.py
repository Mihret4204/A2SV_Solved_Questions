class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        val = 0
        ans = 0

        for i in range(n):
            total+= gas[i] - cost[i]
            val+=  gas[i] - cost[i]
            if val<0:
                val = 0
                ans = i+1
        if total < 0:
            return -1
        return ans