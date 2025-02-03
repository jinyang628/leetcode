# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSametree(self, root: Optional[TreeNode], node: Optional[TreeNode]) -> bool:
        if not root and not node:
            return True
        if not root or not node:
            return False
        if root.val != node.val:
            return False
        return self.isSametree(root.left, node.left) and self.isSametree(root.right, node.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if self.isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)