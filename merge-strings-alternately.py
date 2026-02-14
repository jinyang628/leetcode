1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        res = []
4        word1_idx = word2_idx = 0
5        while word1_idx < len(word1) and word2_idx < len(word2):
6            res.append(word1[word1_idx])
7            res.append(word2[word2_idx])
8            word1_idx += 1
9            word2_idx +=1
10        if word1_idx < len(word1):
11            res.append(word1[word1_idx:])
12        if word2_idx < len(word2):
13            res.append(word2[word2_idx:])
1415        return "".join(res)