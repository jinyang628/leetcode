# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        track = {}
        for i in range(len(inorder)):
            track[inorder[i]] = i
        queue = deque(preorder)
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right or not queue:
                return None
            curr = queue.popleft()
            node = TreeNode(curr)
            node.left = build(left, track[curr] - 1)
            node.right = build(track[curr] + 1, right)
            return node 
        return build(0, len(preorder))