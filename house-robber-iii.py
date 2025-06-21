# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root))
    def helper(self, node: Optional[TreeNode]) -> list[int]:
        # with root, without root
        if not node:
            return [0, 0]
        left_with_root, left_without_root = self.helper(node.left)
        right_with_root, right_without_root = self.helper(node.right)
        return [
            left_without_root + right_without_root + node.val,
            max(left_with_root, left_without_root) + max(right_with_root, right_without_root)
        ]