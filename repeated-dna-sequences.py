from collections import Counter, deque
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        global_counter = Counter()
        queue = deque([])
        right = 0
        while right < len(s):
            queue.append(s[right])
            if len(queue) < 10:
                right += 1
                continue
            global_counter["".join(queue)] += 1
            queue.popleft()
            right += 1
        res = []
        for key, freq in global_counter.items():
            if freq > 1:
                res.append(key)
        return res