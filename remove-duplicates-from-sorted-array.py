1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        counter = Counter(nums)
4        keys = sorted(counter.keys())
5        for i in range(len(keys)):
6            nums[i] = keys[i]
7        return len(keys)