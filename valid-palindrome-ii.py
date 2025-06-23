class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(substring: str) -> bool:
            if not substring:
                return True
            l, r = 0, len(substring) - 1
            while l < r:
                if substring[l] == substring[r]:
                    l += 1
                    r -= 1
                    continue
                return False
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s[left: right]) or isPalindrome(s[left + 1: right + 1])
            left += 1
            right -= 1
        return True