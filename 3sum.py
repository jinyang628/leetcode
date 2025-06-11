class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        i = 0
        res = []
        while i < length - 2:
            j = i + 1
            k = length - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if not curr:
                    res.append([nums[i], nums[j] , nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    continue
                if curr < 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < length - 2 and nums[i] == nums[i - 1]:
                i += 1
        return res