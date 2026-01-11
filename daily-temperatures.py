1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res = [0] * len(temperatures)
4        stack = []
5        for idx, temperature in enumerate(temperatures):
6            while stack and temperature > stack[-1][0]:
7                _, prev_idx = stack.pop()
8                res[prev_idx] = idx - prev_idx
910            stack.append((temperature, idx))
1112        return res
131415