1class Solution:
23    def __init__(self, w: List[int]):
4        self.weights = []
5        self.total = sum(w)
6        curr = 0
7        for num in w:
8            curr += num
9            self.weights.append(curr)
1011    def pickIndex(self) -> int:
12        num = random.uniform(0, self.total)
13        left, right = 0, len(self.weights) - 1
14        while left < right:
15            mid = left + (right - left) // 2
16            if self.weights[mid] < num:
17                left = mid + 1
18            else:
19                right = mid
20        return left
21222324# Your Solution object will be instantiated and called as such:
25# obj = Solution(w)
26# param_1 = obj.pickIndex()