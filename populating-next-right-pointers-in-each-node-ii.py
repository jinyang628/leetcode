"""
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        track = {}
        def dfs(node: 'Node', height: int) -> None:
            if not node:
                return None
            dfs(node.right, height + 1)
            if height not in track:
                track[height] = node
            else:
                node.next = track[height]
                track[height] = node
            dfs(node.left, height + 1)
        dfs(root, 0)
        return track[0]