class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        res = []
        for i in range(len(intervals) - 1):
            first_start, first_end = intervals[i][0], intervals[i][1]
            second_start, second_end = intervals[i + 1][0], intervals[i + 1][1]
            if first_end < second_start:
                res.append(intervals[i])
                continue
            intervals[i + 1][0] = min(first_start, second_start)
            intervals[i + 1][1] = max(first_end, second_end)
        res.append(intervals[-1])
        return res