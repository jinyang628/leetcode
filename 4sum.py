1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        res = []
5        first = 0
6        while first < len(nums) - 3:
7            second = first + 1
8            while second < len(nums) - 2:
9                third = second + 1
10                fourth = len(nums) - 1
11                while third < fourth:
12                    curr = nums[first] + nums[second] + nums[third] + nums[fourth]
13                    if curr == target:
14                        res.append([nums[first], nums[second], nums[third], nums[fourth]])
15                        third += 1
16                        while third < fourth and nums[third] == nums[third - 1]:
17                            third += 1
18                    elif curr > target:
19                        fourth -= 1
20                        while third < fourth and nums[fourth] == nums[fourth + 1]:
21                            fourth -= 1
22                    else:
23                        third += 1
24                        while third < fourth and nums[third] == nums[third - 1]:
25                            third += 1
2627                second += 1
28                while second < len(nums) - 2 and nums[second] == nums[second - 1]:
29                    second += 1
30            first += 1
31            while first < len(nums) - 3 and nums[first] == nums[first - 1]:
32                first += 1
33        return res