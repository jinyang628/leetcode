class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        curr = nums[0]
        for num in nums[1:]:
            count += 1 if num == curr else -1
            if count < 0:
                count = 1
                curr = num
        return curr