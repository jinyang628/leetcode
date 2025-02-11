# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        if not left or not right:
            return False
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if abs(left_height - right_height) <= 1:
            return True
        return False