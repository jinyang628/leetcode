1from collections import Counter
23class Solution:
4    def partitionLabels(self, s: str) -> List[int]:
5        remainder = Counter(s)
6        current = Counter()
7        idx = counter = 0
8        res = []
9        while idx < len(s):
10            counter += 1
11            current[s[idx]] += 1
12            remainder[s[idx]] -= 1
13            is_valid_partition = True
14            for key, freq in current.items():
15                if remainder[key]: 
16                    is_valid_partition = False
17                    break
18            if is_valid_partition:
19                res.append(counter)
20                counter = 0
21                current = Counter()
22            idx += 1
23        return res