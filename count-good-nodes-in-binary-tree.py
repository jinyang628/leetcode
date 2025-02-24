# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], maxSoFar: int) -> int:
            res = 0
            if not node:
                return res
            if node.val >= maxSoFar:
                res += 1
            maxSoFar = max(maxSoFar, node.val)
            res += dfs(node.left, maxSoFar)
            res += dfs(node.right, maxSoFar) 
            return res
        return dfs(root, float('-inf'))