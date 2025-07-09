from collections import deque
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = left = right = 0
        queue = deque([])
        colors += colors[:k - 1]
        while right < len(colors):
            curr = colors[right]
            if len(queue) == k:
                res += 1
                queue.popleft()
                left += 1
                if (k % 2 and curr == queue[0]) or ((not k % 2) and curr != queue[0]):
                    queue.append(curr)
                else:
                    left = right
                    queue = deque([curr])
                right += 1
            else:
                if not queue or curr != queue[-1]:
                    queue.append(curr)
                else:
                    left = right
                    queue = deque([curr])
                right += 1
        return res + 1 if len(queue) == k else res