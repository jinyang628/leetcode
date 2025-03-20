class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        def search(l: int, r: int, isLeftPointer: bool) -> int:
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    if isLeftPointer: 
                        if mid == 0 or nums[mid - 1] < target:
                            return mid
                        r = mid - 1
                    else:
                        if mid == len(nums) - 1 or nums[mid + 1] > target:
                            return mid
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        left_pointer = search(left, right, True)
        right_pointer = search(left, right, False)
        return [left_pointer, right_pointer]