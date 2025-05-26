from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        track = Counter(s)
        total = 0
        for key, freq in track.items():
            if freq == 1 or freq == 2:
                total += freq
                continue
            total += (1 if freq % 2 else 2)
        return total