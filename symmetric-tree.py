1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
9        if not first and not second:
10            return True
11        if not first or not second:
12            return False
13        if first.val != second.val:
14            return False
15        return self.isSameTree(first.left, second.right) and self.isSameTree(first.right, second.left)
1617    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
18        if not root:
19            return True
20        return self.isSameTree(root.left, root.right)
21