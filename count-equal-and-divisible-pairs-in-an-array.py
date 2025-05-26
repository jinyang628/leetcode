class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        total_counter = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] == nums[j] and ((i * j) % k) == 0:
                    total_counter += 1
        return total_counter