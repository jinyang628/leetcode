# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root.left and not root.right:
            return str(root.val)
        res = []
        res.append(str(root.val))
        if not root.left:
            res.append("()")
            res.append(f"({self.tree2str(root.right)})")
        else:
            res.append(f"({self.tree2str(root.left)})")
            if root.right:
                res.append(f"({self.tree2str(root.right)})")
        return "".join(res)