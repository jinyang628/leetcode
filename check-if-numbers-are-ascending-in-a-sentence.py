class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(" ")
        prev = -1
        for word in words:
            if word.isdigit():
                integer = int(word)
                if integer <= prev:
                    return False
                prev = integer
        return True