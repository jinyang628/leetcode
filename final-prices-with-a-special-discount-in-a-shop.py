class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [] # (idx, og price)
        for i in range(len(prices)):
            price = prices[i]
            if not stack:
                stack.append((i, price))
                continue
            while stack and stack[-1][1] >= price:
                idx, p = stack.pop()
                prices[idx] = p - price
            stack.append((i, price))
        return prices