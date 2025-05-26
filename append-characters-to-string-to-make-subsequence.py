class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_pointer = t_pointer = 0
        while t_pointer < len(t) and s_pointer < len(s):
            if s[s_pointer] == t[t_pointer]:
                t_pointer += 1
            s_pointer += 1
        return len(t) - t_pointer