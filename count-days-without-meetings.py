class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[1], x[0]))
        merged = [meetings[0]]
        for i in range(1, len(meetings)):
            start, end = meetings[i]                
            while merged and start <= merged[-1][1]:
                prev_start, _ = merged.pop()
                start = min(prev_start, start)
            merged.append([start, end])
        res = pointer = 0
        i = 1
        while i <= days:
            start, end = merged[pointer]
            if i < start:
                res += (start - i)
            i = end + 1
            pointer += 1
            if pointer >= len(merged):
                res += (days - end)
                break
        return res