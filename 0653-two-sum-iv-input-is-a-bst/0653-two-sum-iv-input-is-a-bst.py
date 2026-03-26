# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        x=[root]
        s=set()
        for i in x:
            if k-i.val in s:
                return True
            s.add(i.val)
            if i.left: x.append(i.left)
            if i.right: x.append(i.right)
            
        return False
            
            
