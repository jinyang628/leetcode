1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        def dfs(node: Optional[TreeNode], maxSoFar: int) -> int: # Return number of good nodes in subtree
10            if not node:
11                return 0
1213            curr_level_res = None
14            if node.val < maxSoFar:
15                curr_level_res = 0
16            else:
17                curr_level_res = 1
1819            maxSoFar = max(maxSoFar, node.val)
20            return curr_level_res + dfs(node.left, maxSoFar) + dfs(node.right, maxSoFar)
2122        return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)