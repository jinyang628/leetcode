# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        track = set()
        def helper(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if node.val in track:
                return True
            track.add(k - node.val)
            return helper(node.left) or helper(node.right)
        return helper(root)