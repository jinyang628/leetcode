1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
9        def build(arr: list[int]) -> Optional[TreeNode]:
10            if not arr:
11                return None
12            mid_idx = len(arr) // 2
13            node = TreeNode(arr[mid_idx])
14            node.left = build(arr[:mid_idx])
15            node.right = build(arr[mid_idx + 1:])
16            return node
17        return build(nums)