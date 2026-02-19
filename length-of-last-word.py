1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        return len(s.strip().split(" ")[-1])