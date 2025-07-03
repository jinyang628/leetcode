class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        track = {}
        mapped = set()
        for i in range(len(s)):
            if s[i] in track:
                if track[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapped:
                    return False
                track[s[i]] = t[i]
                mapped.add(t[i])
        return True