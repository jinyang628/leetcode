from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque([])
        d_queue = deque([])
        for i in range(len(senate)):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        counter = len(senate)
        while r_queue and d_queue:
            first_r, first_d = r_queue.popleft(), d_queue.popleft()
            if first_r < first_d:
                r_queue.append(first_r + counter)
            else:
                d_queue.append(first_d + counter)
            counter += 1
        return "Radiant" if not d_queue else "Dire"