from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        curr = s2[left: right]
        count = Counter(curr)
        target = Counter(s1)
        while right < len(s2):
            if count == target:
                return True
            count[s2[left]] -= 1
            left += 1
            count[s2[right]] += 1
            right += 1
        return count == target