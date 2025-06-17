# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
import heapq
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        track = defaultdict(int) # key is the level, value is the runningSum
        def helper(node: Optional[TreeNode], level: int):
            if not node:
                return
            track[level] += node.val
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)
        values = []
        for val in list(track.values()):
            values.append(-val)
        heapq.heapify(values)
        for _ in range(k):
            if not values:
                return -1
            curr = heapq.heappop(values)
        return -curr