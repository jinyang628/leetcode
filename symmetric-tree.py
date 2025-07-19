# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        level_nodes = defaultdict(list)
        queue = deque([])
        queue.append((root, 1))
        while queue:
            node, level = queue.popleft()
            if node:
                level_nodes[level].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
            else:
                level_nodes[level].append(-101)
        for _, lst in level_nodes.items():
            left = 0
            right = len(lst) - 1
            while left < right:
                if lst[left] != lst[right]:
                    return False
                left += 1
                right -= 1
        return True