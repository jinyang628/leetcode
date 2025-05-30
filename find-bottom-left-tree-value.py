# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxSoFar = [-1, None]
        def helper(node: Optional[TreeNode], level: int):
            if not node:
                return 
            if level > maxSoFar[0]:
                maxSoFar[0] = level
                maxSoFar[1] = node.val
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)
        return maxSoFar[1]