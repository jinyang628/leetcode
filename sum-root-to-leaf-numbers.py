1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumNumbers(self, root: Optional[TreeNode]) -> int:
9        def dfs(node: Optional[TreeNode], path: list[str]) -> int:
10            if not node:
11                path.append(None)
12                return 0
13            path.append(str(node.val))
14            if not node.left and not node.right:
15                return int("".join(path))
16            left = dfs(node.left, path) 
17            path.pop()
18            right = dfs(node.right, path)
19            path.pop()
20            print(left, right)
21            return left + right
22        return dfs(root, [])
23