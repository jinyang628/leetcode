# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node: 'TreeNode') -> Optional['TreeNode']:
            if not node:
                return None
            if (node.val <= p.val and q.val <= node.val) or (node.val <= q.val and p.val <= node.val):
                return node
            if node.val <= p.val:
                return helper(node.right)
            return helper(node.left)
        return helper(root)