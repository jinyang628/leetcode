1class Solution:
2    def merge(self, arr1: list[int], arr2: list[int]) -> list[int]:
3        if not arr1:
4            return arr2
5        if not arr2:
6            return arr1
7        res = []
8        counter1 = counter2 = 0
9        while counter1 < len(arr1) and counter2 < len(arr2):
10            if arr1[counter1] <= arr2[counter2]:
11                res.append(arr1[counter1])
12                counter1 += 1
13            else:
14                res.append(arr2[counter2])
15                counter2 += 1
1617        while counter1 < len(arr1):
18            res.append(arr1[counter1])
19            counter1 += 1
20        while counter2 < len(arr2):
21            res.append(arr2[counter2])
22            counter2 += 1
23        return res
2425    def sortArray(self, nums: List[int]) -> List[int]:
26        if len(nums) <= 1:
27            return nums
28        middleIdx = len(nums) // 2
29        left = self.sortArray(nums[:middleIdx])
30        right = self.sortArray(nums[middleIdx:])
31        return self.merge(left, right)
32