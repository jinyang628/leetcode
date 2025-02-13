class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(substring: str):
            if not substring:
                return False
            left = 0
            right = len(substring) - 1
            while left < right:
                if substring[left] == substring[right]:
                    left += 1
                    right -= 1
                    continue
                return False
            return True
        res = []
        def backtrack(idx: int, path:list[list[int]]):
            print(idx, path)
            if idx == len(s):
                res.append(path[:])
                return 
            for i in range(idx, len(s)):
                if isPalindrome(s[idx: i + 1]):
                    path.append(s[idx: i + 1])
                    backtrack(i + 1, path)
                    path.pop()
        backtrack(0, [])
        return res