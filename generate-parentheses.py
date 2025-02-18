class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(count: int, path: list[str], leftCount: int):
            if count == n * 2:
                if leftCount == 0:
                    res.append("".join(path[:]))
                return
            path.append("(")
            backtrack(count + 1, path, leftCount + 1)
            path.pop()
            if not leftCount:
                return
            path.append(")")
            backtrack(count + 1, path, leftCount - 1)
            path.pop()
        backtrack(0, [], 0)
        return res