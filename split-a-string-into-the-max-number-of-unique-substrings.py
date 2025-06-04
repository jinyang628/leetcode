class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start: int, track: set) -> int:
            if start == len(s):
                return 0
            max_splits = 0
            for end in range(start + 1, len(s) + 1):
                curr = s[start: end]
                if curr in track:
                    continue
                track.add(curr)
                max_splits = max(max_splits, 1 + backtrack(end, track))
                track.remove(curr)
            return max_splits
        return backtrack(0, set())