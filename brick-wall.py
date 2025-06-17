from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        track = defaultdict(int) # key is the position, value is the number of edges seen
        for arr in wall:
            position = 0
            for i in range(len(arr) - 1):
                position += arr[i]
                track[position] += 1
        if track:
            return len(wall) - max(track.values())
        else:
            return len(wall)