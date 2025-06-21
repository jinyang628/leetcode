# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        left1 = root1.left
        right1 = root1.right
        left2 = root2.left
        right2 = root2.right
        return root1.val == root2.val and (
            (self.flipEquiv(left1, left2) and self.flipEquiv(right1, right2)) or
            (self.flipEquiv(left1, right2) and self.flipEquiv(right1, left2))
        )