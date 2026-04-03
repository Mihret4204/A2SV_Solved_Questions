class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        print(nums1)
        nums1.sort()
        if len(nums1)==1:
            return nums1[0]
        if len(nums1)%2==1:
            return float(nums1[len(nums1)//2])
        else:
            a=len(nums1)//2
            ans=nums1[a]+nums1[a-1]
            return ans/2
        return 4.5