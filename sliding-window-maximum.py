from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []
        for idx, num in enumerate(nums):
            while queue and queue[-1] < num:
                queue.pop()
            queue.append(num)
            if idx >= k and nums[idx - k] == queue[0]:
                queue.popleft()
            if idx >= (k - 1):
                res.append(queue[0])
        return res