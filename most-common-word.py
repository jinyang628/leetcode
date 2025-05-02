from collections import defaultdict
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Convert banned list to a set for quick lookup
        banned_set = set(word.lower() for word in banned)
        # Split paragraph into words using regex and normalize to lowercase
        words = re.split(r'[^A-Za-z]+', paragraph.lower())
        # Count word frequencies
        counter = defaultdict(int)
        max_count = 0
        result = ""
        for word in words:
            if word and word not in banned_set:
                counter[word] += 1
                if counter[word] > max_count:
                    max_count = counter[word]
                    result = word
        return result