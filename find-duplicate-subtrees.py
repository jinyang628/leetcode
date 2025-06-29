# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        track = defaultdict(int)
        res = []
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ""
            left = dfs(node.left)
            right = dfs(node.right)
            combined = f"({left}){node.val}({right})"
            if combined in track and track[combined] == 1:
                res.append(node)
            track[combined] += 1
            return combined
        dfs(root)
        return res