class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=[0,0]
        for i in range(len(bills)):
            if bills[i]==5:
                f[0]+=1
            elif bills[i]==10:
                if f[0]<1:
                    return False
                f[0]-=1
                f[1]+=1
            else:
                if f[1]>0 and f[0]>0:
                    f[0]-=1
                    f[1]-=1
                elif f[0]>=3:
                    f[0]-=3
                else:
                    return False
        return True