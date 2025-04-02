class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)
        while right <= len(haystack):
            if needle == haystack[left: right]:
                return left
            left += 1
            right += 1
        return -1