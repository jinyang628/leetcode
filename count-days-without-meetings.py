class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        currDay = 1
        total = 0
        for start, end in meetings:
            if currDay < start:
                total += (start - currDay)
            currDay = max(currDay, end + 1)
        if days >= currDay:
            total += (days - currDay) + 1
        return total