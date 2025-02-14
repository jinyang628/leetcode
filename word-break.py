class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        track = {}
        def backtrack(start: int, end: int) -> bool:
            if (start, end) in track:
                return track[(start, end)]
            if end == len(s):
                return s[start: end] in wordDict
            res = False
            if s[start: end] in wordDict:
                res = res or backtrack(end, end + 1)
            res = res or backtrack(start, end + 1)
            track[(start, end)] = res
            return res
        return backtrack(0, 1)