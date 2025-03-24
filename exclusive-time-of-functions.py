class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_timestamp = 0
        for log in logs:
            id, cmd, timestamp = log.split(":")
            id, timestamp = int(id), int(timestamp)
            if cmd == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_timestamp
                stack.append(id)
                prev_timestamp = timestamp
            else:
                res[stack.pop()] += timestamp - prev_timestamp + 1
                prev_timestamp = timestamp + 1
        return res