# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        left = self.trimBST(root.left, low, high)
        right = self.trimBST(root.right, low, high)
        if root.val < low:
            return right
        if root.val > high:
            return left
        root.left = left
        root.right = right
        return root