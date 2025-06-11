class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        stack = []
        maxSoFar = 0
        for num in nums:
            if not stack:
                stack.append(num)
                continue
            if num > stack[-1]:
                stack.append(num)
            else:
                maxSoFar = max(maxSoFar, sum(stack))
                stack = [num]
        return max(maxSoFar, sum(stack))