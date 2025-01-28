class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        i = 0
        res = []
        while i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if end >= new_start:
                break
            res.append(intervals[i])
            i += 1
        while i in range(len(intervals)):
            if intervals[i][0] > new_end:
                break
            new_start = min(intervals[i][0], newInterval[0])
            new_end = max(intervals[i][1], newInterval[1])
            newInterval[0] = new_start
            newInterval[1] = new_end
            print(new_start)
            print(new_end)
            i += 1
        res.append([new_start, new_end])
        while i in range(len(intervals)):
            res.append(intervals[i])
            i += 1
        return res