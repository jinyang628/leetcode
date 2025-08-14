class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        counter = Counter(words[0])
        for word in words[1:]:
            tmp = Counter(word)
            new_counter = Counter()
            for key in counter:
                if key not in tmp:
                    continue
                new_counter[key] = min(counter[key], tmp[key])
            counter = new_counter
        res = []
        for key, freq in counter.items():
            res.extend([key] * freq)
        return res