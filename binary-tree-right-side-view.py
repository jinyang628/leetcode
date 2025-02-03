# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        track = {} # key is the level, value is the right most value
        def helper(node: Optional[TreeNode], level: int):
            if not node:
                return
            if level not in track:
                track[level] = node.val
            helper(node.right, level + 1)
            helper(node.left, level + 1)
        helper(root, 0)
        res = []
        for _, value in track.items():
            res.append(value)
        return res