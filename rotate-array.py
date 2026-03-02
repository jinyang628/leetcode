1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
45        """
6        k =  k % len(nums)
7        mid = len(nums) - k
8        left, right = 0, len(nums) - 1
9        left_mid_pointer = mid - 1
10        while left < left_mid_pointer:
11            nums[left], nums[left_mid_pointer] = nums[left_mid_pointer], nums[left]
12            left += 1
13            left_mid_pointer -= 1
14        while mid < right:
15            nums[mid], nums[right] = nums[right], nums[mid]
16            mid += 1
17            right -= 1
18        left, right = 0, len(nums) - 1
19        while left < right:
20            nums[left], nums[right] = nums[right], nums[left]
21            left += 1
22            right -= 1
23