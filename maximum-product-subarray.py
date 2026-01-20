1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        maxSoFar = minEndingHere = maxEndingHere = nums[0]
4        for num in nums[1:]:
5            maxEndingHere, minEndingHere = max(
6                maxEndingHere * num, 
7                minEndingHere * num,
89            ), min(
10                maxEndingHere * num,
11                minEndingHere * num,
1213            )
14            maxSoFar = max(maxSoFar, maxEndingHere)
1516        return maxSoFar