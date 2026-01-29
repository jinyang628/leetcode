1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
89    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
10        if not a and not b:
11            return True
12        if not a or not b:
13            return False
14        if a.val != b.val:
15            return False
16        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
17    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
18        if not subRoot and not root:
19            return True
20        if not subRoot and root:
21            return False
22        if not root:
23            return False
24        res = False
25        if root.val == subRoot.val:
26            res = self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
27        res = res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
28        return res