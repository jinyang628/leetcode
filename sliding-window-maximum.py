1from collections import deque
2class Solution:
3    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
4        if k == 1:
5            return nums
6        res = []
7        queue = deque([]) # (num, idx)
8        left = right = 0
9        while right < len(nums):
10            while len(queue) and nums[right] >= queue[-1][0]:
11                queue.pop()
12            queue.append((nums[right], right))
13            right += 1
14            if right >= k:
15                res.append(queue[0][0])
16                left += 1
17                if queue[0][1] < left:
18                    queue.popleft()
19        return res
202122