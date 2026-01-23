1from collections import Counter
2class Solution:
3    def characterReplacement(self, s: str, k: int) -> int:
4        left = right = maxSoFar = 0
5        counter = Counter()
6        mostFreqChar = None
7        while right < len(s):
8            counter[s[right]] += 1
9            if mostFreqChar is None:
10                mostFreqChar = s[right]
11            elif counter[mostFreqChar] < counter[s[right]]:
12                mostFreqChar = s[right]
13            total_chars = right - left + 1
14            num_other_chars = total_chars - counter[mostFreqChar]
15            if num_other_chars <= k:
16                maxSoFar = max(maxSoFar, right - left + 1)
17            else:
18                counter[s[left]] -= 1
19                left += 1
20            right += 1
21        return maxSoFar
22