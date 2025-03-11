class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] >= nums[left]: # left half fully sorted, smaller than nums[mid]
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else: # look for bigger number
                    left = mid + 1
            else: # right half fully sorted, bigger than nums[mid]
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else: # look for smaller number
                    right = mid - 1
        return -1