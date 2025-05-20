class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_track = []
        for i in range(len(s)):
            if s[i] == c:
                c_track.append(i)
        c_pointer = 0
        res = []
        for i in range(len(s)):
            if c == s[i]:
                c_pointer += 1
                res.append(0)
            elif i < c_track[0]:
                res.append(c_track[0] - i)
            elif i > c_track[-1]:
                res.append(i - c_track[-1])
            else:
                res.append(
                    min(
                        i - c_track[c_pointer - 1],
                        c_track[c_pointer] - i
                    )
                )
        return res