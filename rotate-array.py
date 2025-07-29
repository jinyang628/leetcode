class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        """
        k %= len(nums)
        length = len(nums) - 1
        mid = length - k
        copy = mid
        left = 0
        while left < copy:
            nums[left], nums[copy] = nums[copy], nums[left]
            left += 1
            copy -= 1
        copy = mid + 1
        while copy < length:
            nums[copy], nums[length] = nums[length], nums[copy]
            copy += 1
            length -= 1
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1