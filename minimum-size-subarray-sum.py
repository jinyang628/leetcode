1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        left = right = curr = 0
4        minSoFar = float('inf')
5        while left < len(nums) and right < len(nums):
6            print(left, right, curr)
7            curr += nums[right]
8            if curr >= target:
9                minSoFar = min(minSoFar, right - left + 1)
10                curr -= nums[left]
11                curr -= nums[right]
12                left += 1
13            else:
14                right += 1
15        if minSoFar == float('inf'):
16            return 0
17        return minSoFar