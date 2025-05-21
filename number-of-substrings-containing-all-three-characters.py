class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen_a_idx = -1
        last_seen_b_idx = -1
        last_seen_c_idx = -1
        res = 0
        for i in range(len(s)):
            if s[i] == "a":
                last_seen_a_idx = i
            elif s[i] == "b":
                last_seen_b_idx = i
            elif s[i] == "c":
                last_seen_c_idx = i
            if not (last_seen_a_idx == -1 or last_seen_b_idx == -1 or last_seen_c_idx == -1):
                res += min(last_seen_a_idx, last_seen_b_idx, last_seen_c_idx) + 1
        return res