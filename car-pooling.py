from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        depart_track = defaultdict(int)
        arrive_track = defaultdict(int)
        start = float('inf')
        end = float('-inf')
        for num, f, t in trips:
            depart_track[f] += num
            arrive_track[t] += num
            start = min(start, f)
            end = max(end, t)
        curr = 0
        for i in range(start, end + 1):
            curr += depart_track[i]
            curr -= arrive_track[i]
            if curr > capacity:
                return False
        return True