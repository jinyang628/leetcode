class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        use_first_word = True
        i = j = 0
        while i < len(word1) and j < len(word2):
            if use_first_word:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            use_first_word = not use_first_word
        if i < len(word1):
            res += word1[i:]
        if j < len(word2):
            res += word2[j:]
        return res