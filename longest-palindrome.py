from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        track = Counter(s)
        have_odd = False
        res = 0
        for _, freq in track.items():
            if freq % 2 == 1:
                have_odd = True
                res += freq - 1
            else:
                res += freq
        return res + 1 if have_odd else res