1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
9        values = []
10        def dfs(node: Optional[TreeNode]) -> None:
11            if not node:
12                return
13            dfs(node.left)
14            values.append(node.val)
15            dfs(node.right)
16        dfs(root)
17        minDiff = float('inf')
18        for i in range(len(values) - 1):
19            minDiff = min(minDiff, values[i + 1] - values[i])
20        return minDiff
2122