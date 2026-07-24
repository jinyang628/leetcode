1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        best = curr = 0
4        left = right = 0
5        vowels = {"a", "e", "i", "o", "u"}
6        while right < len(s):
7            if s[right] in vowels:
8                curr += 1
9            right += 1
10            best = max(best, curr)
11            if right < k:
12                continue
13            if s[left] in vowels:
14                curr -= 1
15            left += 1
1617        return best