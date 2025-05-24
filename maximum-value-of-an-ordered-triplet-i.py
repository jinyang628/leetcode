class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        leftMax = []
        curr = 0
        for num in nums:
            curr = max(curr, num)
            leftMax.append(curr)
        rightMax = []
        curr = 0
        for num in nums[::-1]:
            curr = max(curr, num)
            rightMax.append(curr)
        rightMax = rightMax[::-1]
        res = 0
        for i in range(1, len(nums) - 1):
            res = max(
                res,
                (leftMax[i - 1] - nums[i]) * rightMax[i + 1]
            )
        return res