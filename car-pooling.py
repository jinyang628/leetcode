from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        depart_track = defaultdict(int) # key is stop, value is number of ppl
        arrival_track = defaultdict(int) # same as above
        for p, d, a in trips:
            depart_track[d] += p
            arrival_track[a] += p
        first_stop = min(depart_track)
        last_stop = max(arrival_track)
        ppl = 0
        print(depart_track)
        print(arrival_track)
        for i in range(first_stop, last_stop):
            if i in depart_track:
                ppl += depart_track[i]
            if i in arrival_track:
                ppl -= arrival_track[i]
            print(ppl)
            if ppl > capacity:
                return False
        return True