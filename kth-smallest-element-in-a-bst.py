1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        res = []
10        def dfs(node: Optional[TreeNode]) -> None:
11            if not node:
12                return
13            dfs(node.left)
14            res.append(node.val)
15            dfs(node.right)
1617        dfs(root)
18        return res[k - 1]
1920