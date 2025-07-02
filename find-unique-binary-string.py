class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        track = set(nums)
        length = len(nums[0])
        all_possible = []
        def backtrack(idx: int, path: list[str]) -> None:
            if idx == length:
                all_possible.append("".join(path))
                return
            path.append("1")
            backtrack(idx + 1, path)
            path.pop()
            path.append("0")
            backtrack(idx + 1, path)
            path.pop()
        backtrack(0, [])
        for num in all_possible:
            if num in track:
                continue
            return num