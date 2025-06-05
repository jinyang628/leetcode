class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print(intervals)
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            last = res[-1]
            if last[0] <= interval[0] and interval[1] <= last[1]:
                continue
            res.append(interval)
        return len(res)