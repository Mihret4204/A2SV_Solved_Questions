# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:      
        _map = {}
        root = {}
        for parent, child, isLeft in descriptions:
            if parent not in _map:
                _map[parent] = TreeNode(parent)
            if child not in _map:
                _map[child] = TreeNode(child)
            if isLeft == 1:
                _map[parent].left = _map[child]
            else:
                _map[parent].right = _map[child]
            if root.get(parent, 0) != -1:
                root[parent] = 1
            root[child] = -1
        rval = 0

        for node, state in root.items():
            if state == 1:
                rval = node
                break

        return _map[rval]