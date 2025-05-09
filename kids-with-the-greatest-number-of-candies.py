class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxSoFar = max(candies)
        res = []
        for i in range(len(candies)):
            candy = candies[i]
            if candy + extraCandies >= maxSoFar:
                res.append(True)
            else:
                res.append(False)
        return res