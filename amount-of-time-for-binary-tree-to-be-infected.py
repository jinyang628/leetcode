from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        total = set()
        neighbors = defaultdict(list)
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            if node.val in total:
                return
            total.add(node.val)
            if node.left:
                neighbors[node.val].append(node.left.val)
                neighbors[node.left.val].append(node.val)
            if node.right:
                neighbors[node.val].append(node.right.val)
                neighbors[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right) 
        dfs(root)
        seen = set()
        res = 0
        queue = deque([])
        queue.append(start)
        while len(seen) != len(total):
            res += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr in seen:
                    continue
                seen.add(curr)
                for neighbor in neighbors[curr]:
                    queue.append(neighbor)
        return res - 1