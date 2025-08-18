# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isWithinBoundary(self, left: int, right: int, node: Optional[TreeNode]) -> bool:
        if not node:
            return True
        if left < node.val < right:
            return self.isWithinBoundary(left, node.val, node.left) and self.isWithinBoundary(node.val, right, node.right)
        return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isWithinBoundary(float('-inf'), float('inf'), root)