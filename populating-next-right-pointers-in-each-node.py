"""
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        track = {} # key is the height, val is the rightmost node so far
        if not root:
            return root
        def pointRight(node: 'Optional[Node]', height: int) -> 'Optional[Node]':
            if not node:
                return node
            if height not in track:
                track[height] = node
            else:
                node.next = track[height]
                track[height] = node
            pointRight(node.right, height + 1)
            pointRight(node.left, height + 1)
        pointRight(root.right, 1)
        pointRight(root.left, 1)
        return root