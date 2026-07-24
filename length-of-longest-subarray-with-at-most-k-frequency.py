1class Solution:
2    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
3        tracker = defaultdict(int)
4        left = right = best = 0
5        while right < len(nums):
6            tracker[nums[right]] += 1
7            while tracker[nums[right]] > k:
8                tracker[nums[left]] -= 1
9                left += 1
10            best = max(right - left + 1, best)
11            right += 1
12        return best
1314