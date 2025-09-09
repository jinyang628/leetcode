"""
"""
# from collections import defaultdict
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        tracker = {}
        def helper(node: Optional[Node], height: int) -> None:
            if not node:
                return 
            if height in tracker:
                tracker[height].next = node 
            tracker[height] = node
            helper(node.left, height + 1)
            helper(node.right, height + 1)
        helper(root, 0)
        return root