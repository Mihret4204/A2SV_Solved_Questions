# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root,total):
            if not root:
                return 0
            
            total+=root.val

            res=prefix.get(total-targetSum,0)
            prefix[total]=prefix.get(total,0)+1
            res+=dfs(root.left,total)+dfs(root.right,total)
            prefix[total]-=1
            if prefix.get(total,0)==0:
                del prefix[total]


            return res
            
        prefix={0:1}
        return dfs(root,0)

