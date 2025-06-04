class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        idx = len(s) - 1
        while idx >= 0:
            if s[idx] == " ":
                break
            idx -= 1
        return len(s) - idx - 1