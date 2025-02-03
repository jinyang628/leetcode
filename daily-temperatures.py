class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        if length <= 1:
            return [0]
        res = [0] * length
        track = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            temp = temperatures[i]
            while track and temp > track[-1][0]:
                _, idx = track.pop()
                res[idx] = i - idx 
            track.append((temp, i))
        return res