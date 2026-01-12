1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        s1_counter = Counter(s1)
4        left = right = 0
5        target_length = len(s1)
6        while right < len(s2):
7            if s1_counter[s2[right]] > 0:
8                s1_counter[s2[right]] -= 1
9                right += 1
10            elif left == right:
11                left += 1
12                right += 1
13            else:
14                s1_counter[s2[left]] += 1
15                left += 1
1617            if right - left == target_length:
18                return True
1920        return False