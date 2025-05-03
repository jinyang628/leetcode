class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def helper(idx1: int, idx2: int, idx3: int) -> bool:
            if idx3 == len(s3):
                return True
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            res = False
            if idx1 < len(s1) and s1[idx1] == s3[idx3]:
                res = helper(idx1 + 1, idx2, idx3 + 1)
            if idx2 < len(s2) and s2[idx2] == s3[idx3]:
                res = res or helper(idx1, idx2 + 1, idx3 + 1)
            memo[(idx1, idx2)] = res
            return res
        return helper(0,0,0)