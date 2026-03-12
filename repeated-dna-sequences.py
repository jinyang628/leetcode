1class Solution:
2    def findRepeatedDnaSequences(self, s: str) -> List[str]:
3        counter = Counter()
4        left = right = 0
5        while right < len(s):
6            if right < 9:
7                right += 1
8                continue
9            counter[s[left: right + 1]] += 1
10            left += 1
11            right += 1
12        res = []
13        for key, freq in counter.items():
14            if freq > 1:
15                res.append(key)
16        return res