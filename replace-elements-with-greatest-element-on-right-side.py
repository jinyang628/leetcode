from collections import deque
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        queue = deque([])
        for num in arr:
            if not queue or queue[-1] >= num:
                queue.append(num)
            else:
                while queue and queue[-1] < num:
                    queue.pop()
                queue.append(num)
        queue.append(-1)
        res = []
        for num in arr:
            if num == queue[0]:
                queue.popleft()
            res.append(queue[0])
        return res