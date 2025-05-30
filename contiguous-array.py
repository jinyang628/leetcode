class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixSums = {}
        total = res = 0
        for i in range(len(nums)):
            total += 1 if nums[i] == 1 else -1
            if not total:
                res = i + 1
            elif total in prefixSums:
                res = max(res, i - prefixSums[total])
            else:
                prefixSums[total] = i
        return res