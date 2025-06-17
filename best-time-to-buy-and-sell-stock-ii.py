class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 2 3 4 5
        stack = []
        profits = 0
        for price in prices:
            if not stack:
                stack.append(price)
            elif price < stack[-1]:
                profits += (stack[-1] - stack[0])
                stack = [price]
            elif len(stack) == 1:
                stack.append(price)
            else:
                stack[-1] = price
        profits += (stack[-1] - stack[0])
        return profits