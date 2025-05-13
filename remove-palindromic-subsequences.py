class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalindrome(input: str) -> bool:
            left = 0
            right = len(input) - 1
            while left < right:
                if input[left] == input[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        if not s:
            return 0
        return 1 if isPalindrome(s) else 2
        return res