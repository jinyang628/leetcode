class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = left = right = res = 0
        length = len(customers)
        for i in range(length):
            if not grumpy[i]:
                base += customers[i]
        while right < length:
            if grumpy[right]:
                base += customers[right]
            right += 1
            if right < minutes:
                continue 
            print(res, base)
            res = max(res, base)
            print(res)
            if grumpy[left]:
                base -= customers[left]
            left += 1
        return res