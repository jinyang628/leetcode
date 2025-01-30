# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(left: int, right: int, node: Optional[TreeNode]):
            if not node:
                return True
            if left >= node.val or node.val >= right:
                return False
            return helper(left, node.val, node.left) and helper(node.val, right, node.right)
        return helper(float('-inf'), float('inf'), root)