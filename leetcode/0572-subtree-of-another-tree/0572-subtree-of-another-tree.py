# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSub(root,subRoot):
            return True
        return  self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)


    def isSub(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None  and subRoot==None :
            return True
        if not root or not subRoot: 
            return False
        if root.val!=subRoot.val:
            return False
       
        return self.isSub(root.left,subRoot.left) and self.isSub(root.right,subRoot.right)