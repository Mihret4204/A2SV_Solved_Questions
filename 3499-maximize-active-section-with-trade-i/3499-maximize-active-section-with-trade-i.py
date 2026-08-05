class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total = Counter(s)
        print(total)
        s='1'+s+'1'
        arr = []
        curr='-1'
        for i in range(1,len(s)-1):
            if arr and  s[i]==arr[-1][0]:
                arr[-1][1]+=1
            else:
                arr.append([s[i],1])
        ans = 0
        mx = 0
        for i in range(1,len(arr)-1):
            if arr[i][0]=='1' and arr[i-1][0]=='0' and arr[i+1][0]=='0':
                mx = max((arr[i-1][1]+arr[i+1][1]),mx)
        return total['1']+mx