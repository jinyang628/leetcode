from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque([i for i in range(1, n + 1)])
        count = k
        while len(queue) > 1:
            curr = queue.popleft()
            count -= 1
            if count:
                queue.append(curr)
            else:
                count = k
        return queue[0]