# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def backtrack(l,r):
            if l>r:
                return None

            mid=l+(r-l)//2
            l=backtrack(l,mid-1)
            r=backtrack(mid+1,r)
            return TreeNode(nums[mid],l,r)

        return backtrack(0,len(nums)-1)
            
            