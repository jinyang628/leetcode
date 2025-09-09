import random
class Solution:
    def __init__(self, w: List[int]):
        total = 0
        prefixSums = []
        for num in w:
            total += num
            prefixSums.append(total)
        self.prefixSums = prefixSums
        self.total = total
    def pickIndex(self) -> int:
        left, right = 0, len(self.prefixSums) - 1
        target = random.randint(1, self.total)
        while left <= right:
            mid = left + (right - left) // 2
            if self.prefixSums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()