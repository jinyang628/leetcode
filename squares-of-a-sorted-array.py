class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort()
        left, right = 0, len(nums) - 1
        res =[]
        while left <= right:
            curr_left = nums[left] ** 2
            curr_right = nums[right] ** 2
            if curr_left >= curr_right:
                res.append(curr_left)
                left += 1
            else:
                res.append(curr_right)
                right -= 1
        return res[::-1]