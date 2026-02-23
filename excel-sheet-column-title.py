1class Solution:
2    def convertToTitle(self, columnNumber: int) -> str:
3        res = []
4        while columnNumber:
5            columnNumber -= 1
6            res.append(
7                chr(ord('A') + columnNumber % 26)
8            )
9            columnNumber //= 26
10        return "".join(reversed(res))