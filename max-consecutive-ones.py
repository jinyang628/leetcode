class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = count = 0
        for num in nums:
            if not num:
                count = 0
            else:
                count += 1
                ans = max(ans, count)
        return ans