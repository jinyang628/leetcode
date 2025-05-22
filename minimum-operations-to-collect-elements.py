from collections import defaultdict
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = num_added = 0
        members = set(num for num in range(1, k + 1))
        track = defaultdict(int)
        while True:
            count += 1
            curr = nums.pop()
            if curr in members and not track[curr]:
                track[curr] += 1
                num_added += 1
            if num_added == k:
                break
        return count