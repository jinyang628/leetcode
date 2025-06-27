from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s) 
        if counter['a'] < k or counter['b'] < k or counter['c'] < k:
            return -1
        for key, freq in counter.items():
            counter[key] -= k
        left = right = maxSoFar = 0
        while right < len(s):
            counter[s[right]] -= 1
            while counter[s[right]] < 0:
                counter[s[left]] += 1
                left += 1
            maxSoFar = max(maxSoFar, right - left + 1)
            right += 1
        if not maxSoFar:
            return len(s)
        return len(s) - maxSoFar