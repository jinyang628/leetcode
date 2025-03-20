class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        """
        k %= len(nums)
        pointer = len(nums) - k - 1
        left = 0
        right = pointer
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        left = pointer + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=  1
            right -= 1