from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        target_counter = Counter(p)
        left = 0
        right = len(p) - 1
        base = Counter(s[left:right])
        res = []
        while right < len(s):
            base[s[right]] += 1
            if target_counter == base:
               res.append(left)
            right += 1
            base[s[left]] -= 1
            if not base[s[left]]:
                del base[s[left]]
            left += 1 
        return res