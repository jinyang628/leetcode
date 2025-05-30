class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x: int) -> int:
            if x < 0:
                return -1
            elif x > 0:
                return 1
            return 0
        curr = 1
        for num in nums:
            curr *= num
        return signFunc(curr)