from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_trust_b_track = defaultdict(list)
        b_trust_a_track = defaultdict(list)
        for a, b in trust:
            a_trust_b_track[a].append(b)
            b_trust_a_track[b].append(a)
        for i in range(1, n + 1):
            if len(b_trust_a_track[i]) == (n - 1) and not a_trust_b_track[i]:
                return i
        return -1