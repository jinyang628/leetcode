1class Solution:
2    def countCharacters(self, words: List[str], chars: str) -> int:
3        bag = Counter(chars)
4        res = 0
5        for word in words:
6            word_bag = Counter(word)
7            total = 0
8            for key, freq in word_bag.items():
9                if key not in bag:
10                    total = 0
11                    break
12                if bag[key] < freq:
13                    total = 0
14                    break
15                total += freq
16            res += total
17        return res
18