1class Solution:
2    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x: (x[1], -x[0]))
4        res = [intervals[0]]
5        for i in range(1, len(intervals)):
6            while res and intervals[i][0] <= res[-1][0]:
7                res.pop()
8            res.append(intervals[i])
9        return len(res)