import heapq
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        S = sum(milestones)
        M = max(milestones)
        return 2 * (S - M) + 1 if M > S - M else S