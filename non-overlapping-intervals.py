class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        res = 0
        for i in range(1, len(intervals)):
            first_end = intervals[i - 1][1]
            second_start = intervals[i][0]
            if first_end <= second_start:
                continue
            intervals[i] = intervals[i - 1]
            res += 1
        return res