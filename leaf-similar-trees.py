# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaves(self, node: Optional[TreeNode]) -> list[int]:
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        left_leaves = self.getLeaves(node.left)
        right_leaves = self.getLeaves(node.right)
        return left_leaves + right_leaves
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        one_leaves = self.getLeaves(root1)
        two_leaves = self.getLeaves(root2)
        if len(one_leaves) != len(two_leaves):
            return False
        for i in range(len(one_leaves)):
            if one_leaves[i] != two_leaves[i]:
                return False
        return True