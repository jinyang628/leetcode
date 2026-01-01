1class Solution(object):
2    def twoSum(self, numbers, target):
3        """
4567        """
8        res = [None, None]
9        for i in range(len(numbers)):
10            new_target = target - numbers[i]
11            left, right = i + 1, len(numbers) - 1
12            while left <= right:
13                mid = left + (right - left) // 2
14                if numbers[mid] == new_target:
15                    res[0] = i + 1
16                    res[1] = mid + 1
17                    return res
18                elif numbers[mid] < new_target:
19                    left = mid + 1
20                else:
21                    right = mid - 1