class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left, right = 0, len(word) - 1
            isPalindrome = True
            while left < right:
                if word[left] != word[right]:
                    isPalindrome = False
                    break
                left += 1
                right -= 1
            if isPalindrome:
                return word
        return ""