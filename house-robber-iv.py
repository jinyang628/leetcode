1class Solution:
2    def minCapability(self, nums: List[int], k: int) -> int:
3        left, right = min(nums), max(nums)
4        # best
5        while left <= right:
6            mid = left + (right - left) // 2
7            prev_idx = -2
8            freq = 0
9            for idx, num in enumerate(nums):
10                if num <= mid and prev_idx + 1 < idx:
11                    prev_idx = idx
12                    freq += 1
13                if freq == k:
14                    break
15            if freq == k:
16                right = mid - 1
17            else:
18                left = mid + 1
19        return left
20