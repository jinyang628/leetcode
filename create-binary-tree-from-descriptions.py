# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        in_order = defaultdict(int)
        nodes = {} # key is node val, value is the actual node
        for parent, child, isLeft in descriptions:
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            in_order[child] += 1
        for par, _, _ in descriptions:
            if not in_order[par]: # root has in order degree of 0
                return nodes[par]