# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        track = {} # key is the level, value is the prev seen node val
        def helper(node: Optional[TreeNode], level: int) -> bool:
            if not node:
                return True
            if level % 2: # odd
                if node.val % 2 == 1:
                    return False
                if level not in track:
                    track[level] = node.val
                elif track[level] <= node.val:
                    return False
                else:
                    track[level] = node.val
            else:
                if node.val % 2 == 0:
                    return False
                if level not in track:
                    track[level] = node.val
                elif track[level] >= node.val:
                    return False
                else:
                    track[level] = node.val
            return helper(node.left, level + 1) and helper(node.right, level + 1)
        return helper(root, 0)