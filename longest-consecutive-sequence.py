class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        track = set()
        nums = set(nums)
        for num in nums:
            curr = num
            if curr in track:
                continue
            while curr - 1 in nums:
                curr -= 1
            count = 0
            while curr in nums:
                count += 1
                track.add(curr)
                curr += 1
            res = max(res, count)
        return res