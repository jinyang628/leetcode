from collections import defaultdict
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def get_sum(s: str):
            sum = 0
            for char in s:
                print(char)
                sum += int(char)
            return sum
        track = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            bucket = get_sum(str(i))
            track[bucket] += 1
        return max(track.values())