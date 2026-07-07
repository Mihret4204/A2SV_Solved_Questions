class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        arr=[]
        total=0
        while n!=0:
            rem = n%10
            if rem !=0:
                total+=rem
                arr.append(str(rem))   
            n//=10
            
        arr.reverse()
        res = 0
        if arr:
            res = int("".join(arr))
       
        return res * total