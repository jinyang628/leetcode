class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_pointer = t_pointer = 0
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                s_pointer += 1
        return len(t) - t_pointer