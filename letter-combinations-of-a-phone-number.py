1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        digits_to_alphabets = {
4            "2": ["a", "b", "c"],
5            "3": ["d", "e", "f"],
6            "4": ["g", "h", "i"],
7            "5": ["j", "k", "l"],
8            "6": ["m", "n", "o"],
9            "7": ["p", "q", "r", "s"],
10            "8": ["t", "u", "v"],
11            "9": ["w", "x", "y", "z"]
12        }
13        res = []
14        def backtrack(idx: int, path: list[str]) -> None:
15            if idx == len(digits):
16                res.append("".join(path))
17                return
18            alphabets = digits_to_alphabets[digits[idx]]
19            for alphabet in alphabets:
20                path.append(alphabet)
21                backtrack(idx + 1, path)
22                path.pop()
2324        backtrack(0, [])
25        return res