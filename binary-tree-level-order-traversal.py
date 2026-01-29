1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11        res = []
12        tracker = defaultdict(list)
13        queue = deque([(1, root)])
14        while queue:
15            level, curr = queue.popleft()
16            tracker[level].append(curr.val)
17            if curr.left:
18                queue.append((level + 1, curr.left))
19            if curr.right:
20                queue.append((level + 1, curr.right))
2122        for _, nodes in sorted(tracker.items()):
23            res.append(nodes)
24        return res
25