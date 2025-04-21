from collections import defaultdict
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        track = defaultdict(int)
        for val, weight in items1:
            track[val] += weight
        for val, weight in items2:
            track[val] += weight
        res = []
        for val, weight in track.items():
            res.append([val, weight])
        return sorted(res)