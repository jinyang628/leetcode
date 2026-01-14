1"""
234567"""
89from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        if not node:
13            return node
1415        tracker = {} # key is the original node's, value is the cloned node
16        def dfs_build(n: Optional['Node']) -> None:
17            if not n:
18                return
19            if n.val in tracker:
20                return 
21            tracker[n.val] = Node(n.val)
22            for neighbor in n.neighbors:
23                dfs_build(neighbor)
24        dfs_build(node)
2526        visited = set()
27        def dfs_connect(n: Optional['Node']) -> None:
28            if not n:
29                return
30            if n.val in visited:
31                return
32            visited.add(n.val)
33            cloned_current_node = tracker[n.val]
34            for neighbor in n.neighbors:
35                cloned_current_node.neighbors.append(tracker[neighbor.val])
36                dfs_connect(neighbor)
3738        dfs_connect(node)
39        return tracker[node.val]
40