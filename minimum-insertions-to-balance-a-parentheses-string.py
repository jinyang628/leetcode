class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        res = i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if not stack:
                    if i != len(s) - 1 and s[i + 1] == ")":
                        i += 1
                        res += 1
                    else:
                        res += 2
                else:
                    if i != len(s) - 1 and s[i + 1] == ")":
                        stack.pop()
                        i += 1
                    else:
                        stack.pop()
                        res += 1
            i += 1
        return res + len(stack) * 2