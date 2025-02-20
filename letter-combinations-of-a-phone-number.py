class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        track = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        res = []
        def backtrack(idx: int, path: list[str]):
            if idx == len(digits):
                res.append("".join(path))
                return
            currDigit = digits[idx]
            for char in track[currDigit]:
                path.append(char)
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0, [])
        return res