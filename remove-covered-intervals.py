1class Solution:
2    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x: (x[0], -x[1]))
4        removed_intervals = set()
5        for i in range(len(intervals) - 1):
6            if i in removed_intervals:
7                continue
8            start, end = intervals[i]
9            for j in range(i + 1, len(intervals)):
10                if start <= intervals[j][0] and intervals[j][1] <= end:
11                    removed_intervals.add(j)
1213        return len(intervals) - len(removed_intervals)