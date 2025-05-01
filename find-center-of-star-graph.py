from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        track = defaultdict(list)
        for a, b in edges:
            track[a].append(b)
            track[b].append(a)
        for key, value in track.items():
            if len(value) == (len(track) - 1):
                return key