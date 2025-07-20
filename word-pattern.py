class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapped_words = set()
        mappings = {}
        splitted = s.split(" ")
        if len(pattern) != len(splitted):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mappings:
                if mappings[pattern[i]] == splitted[i]:
                    continue
                return False
            if splitted[i] in mapped_words:
                return False
            mapped_words.add(splitted[i])
            mappings[pattern[i]] = splitted[i]
        return True