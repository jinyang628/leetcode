class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        """
        zero_pointer = 0
        one_pointer = 0
        two_pointer = len(nums) - 1
        while one_pointer <= two_pointer:
            if nums[one_pointer] == 0:
                nums[zero_pointer], nums[one_pointer]= nums[one_pointer], nums[zero_pointer]
                zero_pointer += 1
                one_pointer += 1
            elif nums[one_pointer] == 2:
                nums[two_pointer], nums[one_pointer] = nums[one_pointer], nums[two_pointer]
                two_pointer -= 1
            else:
                one_pointer +=1
        return nums