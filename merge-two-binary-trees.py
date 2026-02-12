1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root1 and not root2:
10            return None
11        if root1 and not root2:
12            left = self.mergeTrees(root1.left, None)
13            right = self.mergeTrees(root1.right, None)
14            node = TreeNode(root1.val, left, right)
15            return node
16        elif root2 and not root1:
17            left = self.mergeTrees(root2.left, None)
18            right = self.mergeTrees(root2.right, None)
19            node = TreeNode(root2.val, left, right)
20            return node
21        else:
22            left = self.mergeTrees(root1.left, root2.left)
23            right = self.mergeTrees(root1.right, root2.right)
24            node = TreeNode(root1.val + root2.val, left, right)
25            return node