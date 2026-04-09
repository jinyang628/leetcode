1class Solution:
2    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
3        res = []
4        for x, y in points:
5            res.append(x)
67        res.sort()
8        maximum = 0
9        for i in range(len(res) - 1):
10            maximum = max(maximum, res[i + 1] - res[i])
11        return maximum