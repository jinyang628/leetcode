class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        close_to_open = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        i = 0
        stack=[]
        while i < len(s):
            curr = s[i]
            if curr in open_to_close:
                stack.append(curr)
            elif curr in close_to_open:
                if not stack:
                    return False
                last = stack.pop()
                if close_to_open[curr] != last:
                    return False
            else:
                raise ValueError("Invalid input")
            i += 1
        return True if not stack else False