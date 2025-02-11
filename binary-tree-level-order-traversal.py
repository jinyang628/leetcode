# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        track = defaultdict(list)
        def helper(node: Optional[TreeNode], height: int):
            if not node:
                return
            track[height].append(node.val)
            helper(node.left, height + 1)
            helper(node.right, height + 1)
        helper(root, 0)
        for height, lst in track.items():
            res.append(lst)
        return res