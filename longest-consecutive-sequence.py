1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        tracker = {} # key is the largest number in descending consecurive order, value is the length
4        visited = set()
5        nums = set(nums)
6        maxSoFar = 0
7        for num in nums:
8            if num in visited:
9                continue
1011            original = num
12            curr = 0
13            while num in nums:
14                if num in tracker:
15                    curr += tracker[num]
16                    break
17                visited.add(num)
18                num -= 1
19                curr += 1
2021            maxSoFar = max(maxSoFar, curr)
22            tracker[original] = curr
2324        return maxSoFar
25