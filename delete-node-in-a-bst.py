# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            if root.left and root.right:
                root.val = self.getMin(root.right)
                root.right = self.deleteNode(root.right, root.val)
            else:
                return root.left if root.left else root.right
        return root
    def getMin(self, root: TreeNode) -> int:
        while root:
            last = root.val
            root = root.left
        return last