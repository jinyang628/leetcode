1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        track = defaultdict(int)
10        def dfs(node: Optional[TreeNode], level: int) -> None:
11            if not node:
12                return
13            if level not in track:
14                track[level] = node.val
15            dfs(node.right, level + 1)
16            dfs(node.left, level + 1)
171819        dfs(root, 0)
20        res = []
21        for _, val in sorted(track.items()):
22            res.append(val)
23        return res