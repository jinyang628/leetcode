class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = maxSoFar = 0 
        while right < len(nums):
            print(left, right)
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            maxSoFar = max(maxSoFar, right - left + 1)
            right += 1
        return maxSoFar