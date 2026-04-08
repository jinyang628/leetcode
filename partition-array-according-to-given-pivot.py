1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        smaller = []
4        same = []
5        larger = []
6        for num in nums:
7            if num < pivot:
8                smaller.append(num)
9            elif num > pivot:
10                larger.append(num)
11            else:
12                same.append(num)
13        return smaller + same + larger