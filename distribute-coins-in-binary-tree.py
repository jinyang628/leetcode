1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
89    def distributeCoins(self, root: Optional[TreeNode]) -> int:
10        self.ans = 0
11        self.getExcess(root)
12        return self.ans
1314    def getExcess(self, root: Optional[TreeNode]) -> int:
15        if not root:
16            return 0
17        leftExcess = self.getExcess(root.left)
18        rightExcess = self.getExcess(root.right)
19        self.ans += abs(leftExcess) + abs(rightExcess)
20        return leftExcess + rightExcess + root.val - 1