class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = res = 0
        product = 1
        while right < len(nums):
            product *= nums[right]
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            res += (right - left + 1)
            right += 1
        return res