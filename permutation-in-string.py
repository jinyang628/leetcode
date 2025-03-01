from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        left = 0
        right = len(s1)
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:right])
        while right < len(s2):
            if s1_counter == s2_counter:
                return True
            s2_counter[s2[left]] -= 1
            if not s2_counter[s2[left]]:
                del s2_counter[s2[left]]
            left += 1
            s2_counter[s2[right]] += 1
            right += 1
        return s1_counter == s2_counter