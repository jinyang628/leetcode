class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_track = {}
        t_track = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in s_track:
                s_track[s[i]] = i
            if t[i] not in t_track:
                t_track[t[i]] = i
            if s_track[s[i]] != t_track[t[i]]:
                return False
        return True