class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        print(nums)
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while nums[j + 1] == nums[j] and j < len(nums) - 2:
                        j += 1 
                    while nums[k - 1] == nums[k] and k > 0:
                        k -= 1
                    j += 1
                    k -= 1
                elif curr > 0 :
                    k -= 1
                else:
                    j += 1
            while nums[i + 1] == nums[i] and i < len(nums) - 2:
                i += 1
            i += 1
        return res