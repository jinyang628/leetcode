1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        left = 0
5        res = []
6        while left < len(nums) - 2:
7            mid = left + 1
8            right = len(nums) - 1
9            while mid < right:
10                curr_sum = nums[left] + nums[mid] + nums[right] 
11                if curr_sum == 0:
12                    res.append([nums[left], nums[mid], nums[right]])
13                    mid += 1
14                    right -= 1
15                    while mid < right and nums[mid] == nums[mid - 1]:
16                        mid += 1
17                    while mid < right and nums[right] == nums[right + 1]:
18                        right -= 1
19                elif curr_sum < 0:
20                    mid += 1
21                else:
22                    right -= 1
2324            left += 1
25            while left < len(nums) - 2 and nums[left] == nums[left - 1]:
26                left += 1
27        return res
2829