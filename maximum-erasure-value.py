class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefixSums = [0]
        sumSoFar = 0
        for num in nums:
            sumSoFar += num
            prefixSums.append(sumSoFar)
        left = right = score = 0
        track = set()
        while right < len(nums):
            if nums[right] in track:
                while True:
                    removed = nums[left]
                    track.remove(removed)
                    left += 1
                    if removed == nums[right]:
                        break
            track.add(nums[right])
            right += 1
            score = max(score, prefixSums[right] - prefixSums[left])
        return score