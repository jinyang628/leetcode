1from collections import deque
2class Solution:
3    def replaceElements(self, arr: List[int]) -> List[int]:
4        largestSoFar = deque([])
5        maxSoFar = arr[-1]
6        for num in arr[::-1]:
7            maxSoFar = max(maxSoFar, num)
8            largestSoFar.appendleft(maxSoFar)
9        res = []
10        for i in range(len(arr) - 1):
11            res.append(largestSoFar[i + 1])
12        res.append(-1)
13        return res