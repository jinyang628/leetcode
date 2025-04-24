from collections import deque
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: [x[1], x[0]])
        res = 0
        queue = deque([])
        for pair in pairs:
            queue.append(pair)
        prevEnd = float('-inf')
        while queue:
            start, end = queue.popleft()
            if start > prevEnd:
                prevEnd = end 
                res += 1
        return res