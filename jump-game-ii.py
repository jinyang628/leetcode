class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = farthest = count = 0
        while far < len(nums) - 1:
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            near = far + 1
            far = farthest
            count += 1
        return count