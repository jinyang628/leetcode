class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            left_candidate = nums[left] ** 2
            right_candidate = nums[right] ** 2
            if left_candidate <= right_candidate:
                res.append(right_candidate)
                right -= 1
            else:
                res.append(left_candidate)
                left += 1
        return res[::-1]