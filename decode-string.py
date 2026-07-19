1class Solution:
2    def decodeString(self, s: str) -> str:
3        def construct(index: int) -> tuple[str, int]:
4            res = ""
5            multiplier = ""
6            while index < len(s) and s[index] != "]":
7                if s[index].isdigit():
8                    multiplier += s[index]
9                elif s[index] == "[":
10                    index += 1
11                    substring, index = construct(index)
12                    res += int(multiplier) * substring
13                    multiplier = ""
14                else:
15                    res += s[index]
16                index += 1
17            return res, index
18        res, _ = construct(0)
19        return res
20