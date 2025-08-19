class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        turns_required = tickets[k]
        res = 0
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], turns_required)
            else:
                res += min(tickets[i], turns_required - 1)
        return res