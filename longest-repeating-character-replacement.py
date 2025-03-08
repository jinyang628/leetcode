from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = left = right = 0
        track = defaultdict(int)
        track[s[right]] += 1
        while right < len(s):
            max_value = max(track.values())
            if right - left + 1 - max_value <= k:
                res = max(res, right - left + 1)
                right += 1
                if right < len(s):
                    track[s[right]] += 1
                continue
            track[s[left]] -= 1
            left += 1
        return res