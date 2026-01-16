1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        track = {} # key is the value we are looking for, value is the other index
4        for idx, num in enumerate(nums):
5            if num in track:
6                return [idx, track[num]]
7            track[target - num] = idx
8