1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def getHeight(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
1112        left = self.getHeight(root.left)
13        right = self.getHeight(root.right)
14        return max(left, right) + 1
1516    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
17        if not root:
18            return 0
19        left = self.diameterOfBinaryTree(root.left)
20        right = self.diameterOfBinaryTree(root.right)
21        return max(
22            left,
23            right,
24            self.getHeight(root.left) + self.getHeight(root.right)
25        )
26