class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def backtrack(idx: int, path: list[int]) -> None:
            if idx > n:
                res.append("".join(path))
                return
            if not path or path[-1] != "a":
                path.append("a")
                backtrack(idx + 1, path)
                path.pop()
            if not path or path[-1] != "b":
                path.append("b")
                backtrack(idx + 1, path)
                path.pop()
            if not path or path[-1] != "c":
                path.append("c")
                backtrack(idx + 1, path)
                path.pop()
        backtrack(1, [])
        res.sort()
        if k - 1 >= len(res):
            return ""
        return res[k - 1]