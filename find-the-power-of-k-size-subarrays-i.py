from collections import deque
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []
        for i in range(len(nums)):
            num = nums[i]
            if not queue or queue[-1] == num - 1:
                queue.append(num)
            else:
                queue = deque([])
                queue.append(num)
            if len(queue) != k:
                if i >= (k - 1):
                    res.append(-1)
                continue 
            res.append(queue[-1])
            queue.popleft()
        return res