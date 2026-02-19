1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        suffixSum = 0
10        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
11            nonlocal suffixSum
12            if not node:
13                return None
14            dfs(node.right)
15            suffixSum += node.val
16            node.val = suffixSum
17            dfs(node.left)
18            return node
19        return dfs(root)