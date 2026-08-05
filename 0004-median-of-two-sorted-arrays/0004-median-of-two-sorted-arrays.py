class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n ==1:
            return nums1[0]
        if n %2==1:
            return float(nums1[n//2])
        else:
            a=n//2
            ans=nums1[a]+nums1[a-1]
            return ans/2
        