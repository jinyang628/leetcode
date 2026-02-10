1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        pattern_to_word = defaultdict(set)
4        word_to_pattern = defaultdict(set)
5        s = s.split(" ")
6        if len(pattern) != len(s):
7            return False
8        for idx, char in enumerate(pattern):
9            pattern_to_word[char].add(s[idx])
10            word_to_pattern[s[idx]].add(char)
11        if len(pattern_to_word) != len(word_to_pattern):
12            return False 
13        for key, items in pattern_to_word.items():
14            if len(items) != 1:
15                return False
16        for key, items in word_to_pattern.items():
17            if len(items) != 1:
18                return False
19        return True