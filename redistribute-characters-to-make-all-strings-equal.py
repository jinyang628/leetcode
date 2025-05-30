from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        count = Counter()
        for word in words:
            count += Counter(word)
        for _, freq in count.items():
            if freq % length != 0:
                return False
        return True