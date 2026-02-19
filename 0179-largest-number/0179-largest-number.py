class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        list1=[]
        ans=""
        for num in nums:
            list1.append(str(num))
        list1.sort(key=cmp_to_key(lambda n1,n2: 1 if n1+n2>n2+n1 else -1))
        list1=list1[::-1]
        for i in range(len(list1)):
            ans+=list1[i]
            print(i)
        if ans[0] == "0":
            return "0"
        return ans
        