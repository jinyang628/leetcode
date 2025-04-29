from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ones = Counter(words1)
        twos = Counter(words2)
        res = 0
        for word, freq in ones.items():
            if freq > 1:
                continue
            if word not in twos:
                continue
            if twos[word] == 1:
                res += 1
        return res