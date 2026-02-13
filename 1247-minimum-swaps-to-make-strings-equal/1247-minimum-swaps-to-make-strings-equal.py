class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy=0
        yx=0
        count=0
        for i in range(len(s1)):
            if s1[i]=="x" and s2[i]=="y":
                xy+=1
            elif s1[i]=="y" and s2[i]=="x":
                yx+=1
            else:
                continue 
        print(xy)
        if (xy + yx)%2!=0:
            return -1

        if xy%2==0 :
            count=xy//2+yx//2
        else:
            count=xy//2+yx//2+2
            
        return count    