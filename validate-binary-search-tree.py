1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        def dfs(left: float, right: float, node: Optional[TreeNode]) -> bool:
10            if not node:
11                return True
12            if left < node.val < right:
13                return dfs(left, node.val, node.left) and dfs(node.val, right, node.right)
14            return False
1516        return dfs(float('-inf'), float('inf'), root)