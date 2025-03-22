class Node:
    def __init__(self, val: int, left: Optional["Node"], right: Optional["Node"]):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def numTrees(self, n: int) -> int:
        track = {}
        def helper(l: int, r: int) -> int:
            counter = 0
            if l >= r:
                return 1
            if (l, r) in track:
                return track[(l, r)]
            for i in range(l, r):
                left = helper(l, i)
                right = helper(i + 1, r)
                counter += left * right
            track[(l, r)] = counter
            return counter
        return helper(1, n + 1)