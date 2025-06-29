class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        original = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                original += customers[i]
        maxSoFar = original
        left = right = currBonus = 0
        while right < len(customers):
            if grumpy[right]:
                currBonus += customers[right]
            if (right - left + 1) < minutes:
                right += 1
                continue 
            maxSoFar = max(maxSoFar, original + currBonus)
            if grumpy[left]:
                currBonus -= customers[left]
            left += 1
            right += 1
        return maxSoFar