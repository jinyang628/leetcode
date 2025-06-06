from collections import Counter
class Solution:
    def minimumSteps(self, s: str) -> int:
        count = Counter(s)
        targetWhiteIdxSum = (count["0"] * (count["0"] - 1)) // 2
        actualWhiteIdxSum = 0
        for i in range(len(s)):
            if s[i] == "0":
                actualWhiteIdxSum += i
        return abs(targetWhiteIdxSum - actualWhiteIdxSum)