1class Solution:
2    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
3        ratios = defaultdict(float)
4        res = 0
5        for w, h in rectangles:
6            ratio = w / h
7            res += ratios[ratio]
8            ratios[ratio] += 1
9        return int(res)