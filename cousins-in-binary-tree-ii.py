# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depthSum = defaultdict(int)
        def calculateDepthSum(node: Optional[TreeNode], depth: int):
            if not node:
                return
            depthSum[depth] += node.val
            calculateDepthSum(node.left, depth + 1)
            calculateDepthSum(node.right, depth + 1)
        calculateDepthSum(root, 0)
        def assignCousinsSum(node: Optional[TreeNode], depth: int) -> Optional[TreeNode]:
            if not node:
                return node
            subtractedValue = 0
            if node.left:
                subtractedValue += node.left.val
            if node.right:
                subtractedValue += node.right.val
            cousinsSum = depthSum[depth + 1] - subtractedValue
            if node.left:
                node.left.val = cousinsSum
                assignCousinsSum(node.left, depth + 1)
            if node.right:
                node.right.val = cousinsSum
                assignCousinsSum(node.right, depth + 1)
            return node
        root.val = 0
        return assignCousinsSum(root, 0)