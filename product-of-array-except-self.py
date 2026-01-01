1class Solution(object):
2    def productExceptSelf(self, nums):
3        """
456        """
7        prefixProducts = [0] * len(nums)
8        curr = 1
9        for i in range(len(nums)):
10            prefixProducts[i] = curr
11            curr *= nums[i]
12        curr = 1
13        for i in range(len(nums) - 1, -1, -1):
14            prefixProducts[i] *= curr
15            curr *= nums[i]
16        return prefixProducts