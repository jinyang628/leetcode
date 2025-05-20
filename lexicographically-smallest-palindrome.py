class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        res = [None] * len(s)
        while left <= right:
            if s[left] == s[right]:
                res[left] = s[left]
                res[right] = s[right]
            else:
                if s[left] < s[right]:
                    res[right] = s[left]
                    res[left] = s[left]
                else:
                    res[left] = s[right]
                    res[right] = s[right]
            left += 1
            right -= 1
        return "".join(res)