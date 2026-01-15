1from collections import Counter
2class Solution:
3    def lengthOfLongestSubstring(self, s: str) -> int:
4        left = right = maxSoFar = 0
5        counter = Counter()
6        while right < len(s):
7            counter[s[right]] += 1
8            while counter[s[right]] > 1:
9                counter[s[left]] -= 1
10                left += 1
11            maxSoFar = max(maxSoFar, right - left + 1)
12            right += 1
1314        return maxSoFar
1516