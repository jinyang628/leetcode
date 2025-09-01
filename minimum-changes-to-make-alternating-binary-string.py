class Solution:
    def minOperations(self, s: str) -> int:
        first = second = 0
        for i in range(len(s)):
            curr = s[i]
            if i % 2:
                if curr == "0":
                    continue
            else:
                if curr == "1":
                    continue
            first += 1
        for i in range(len(s)):
            curr = s[i]
            if i % 2:
                if curr == "1":
                    continue
            else:
                if curr == "0":
                    continue
            second += 1
        return min(first, second)