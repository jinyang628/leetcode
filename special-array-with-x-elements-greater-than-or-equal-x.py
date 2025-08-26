class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def count_numbers_gr_or_equal_to_x(x):
            return sum(num >= x for num in nums)
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if count_numbers_gr_or_equal_to_x(mid) <= mid:
                right = mid
            else:
                left = mid + 1
        return left if count_numbers_gr_or_equal_to_x(left) == left else -1