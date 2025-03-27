# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def helper(node: Optional[TreeNode], numbersSoFar: list[str]):
            if not node:
                return
            numbersSoFar.append(str(node.val))
            if not node.left and not node.right:
                res.append(
                    int("".join(numbersSoFar))
                )
                numbersSoFar.pop()
                return
            helper(node.left, numbersSoFar)
            helper(node.right, numbersSoFar)
            numbersSoFar.pop()
        helper(root, [])
        print(res)
        return sum(res)