class Solution:
    def maxDepth(self, s: str) -> int:
        counter = res = 0
        for char in s:
            if char == "(":
                counter += 1
                res = max(res, counter)
            elif char == ")":
                counter -= 1
        return res