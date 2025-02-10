"""
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        track = {}
        def dfs(n: Optional['Node']):
            if not n:
                return 
            if n.val in track:
                return
            track[n.val] = Node(n.val)
            for neighbor in n.neighbors:
                dfs(neighbor)
        dfs(node)
        seen = set()
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr.val in seen:
                continue
            seen.add(curr.val)
            for neighbor in curr.neighbors:
                mapped_neighbor = track[neighbor.val]
                track[curr.val].neighbors.append(mapped_neighbor)
                stack.append(neighbor)
        return track[1]