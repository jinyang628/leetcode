class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        def isPalindrome(l: int, r: int) -> bool:
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            return isPalindrome(left + 1, right) or isPalindrome(left, right -1)
        return True