1class Solution:
2    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
3        remainders = {0: -1} # key is remainder, value is index
4        curr = 0
5        for idx, num in enumerate(nums):
6            curr += num
7            remainder = curr % k 
8            if remainder in remainders and remainders[remainder] + 2 <= idx:
9                return True
10            if remainder not in remainders:
11                remainders[remainder] = idx
12        return False